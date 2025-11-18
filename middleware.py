import os
import asyncio
import websockets
import json
from fastapi import FastAPI, WebSocket
from fastapi.responses import FileResponse
import uvicorn
from starlette.websockets import WebSocketDisconnect
from dotenv import load_dotenv
from deepgram import DeepgramClient

load_dotenv()

app = FastAPI()
API_KEY = os.getenv("DEEPGRAM_API_KEY")

# Serve the web client
@app.get("/")
async def get_web_client():
    return FileResponse("web_client.html")

@app.websocket("/stream")
async def audio_stream(ws: WebSocket):
    await ws.accept()
    print("[CALL] Started - Client connected")
    
    # Connect to Deepgram streaming
    deepgram_url = f"wss://api.deepgram.com/v1/listen?model=nova-2&language=multi&smart_format=true&interim_results=true&punctuate=true&encoding=linear16&sample_rate=16000"
    
    full_transcript = []
    
    try:
        async with websockets.connect(
            deepgram_url,
            additional_headers={"Authorization": f"Token {API_KEY}"}
        ) as dg_ws:
            print("[DEEPGRAM] Connected to streaming API")
            
            # Task to receive from Deepgram
            async def receive_from_deepgram():
                async for message in dg_ws:
                    data = json.loads(message)
                    
                    if "channel" in data:
                        transcript = data["channel"]["alternatives"][0]["transcript"]
                        if len(transcript) > 0:
                            confidence = data["channel"]["alternatives"][0]["confidence"]
                            is_final = data.get("is_final", False)
                            
                            print(f"[TRANSCRIPT] {'[FINAL]' if is_final else '[INTERIM]'} {transcript}")
                            
                            # Send to web client
                            await ws.send_json({
                                "type": "transcript",
                                "text": transcript,
                                "confidence": confidence,
                                "is_final": is_final
                            })
                            
                            if is_final:
                                full_transcript.append(transcript)
            
            # Task to send to Deepgram
            async def send_to_deepgram():
                while True:
                    message = await ws.receive()
                    
                    if "bytes" in message:
                        await dg_ws.send(message["bytes"])
                    elif "text" in message and message["text"] == "END":
                        print("[CALL] Ended")
                        return
            
            # Run both tasks concurrently
            await asyncio.gather(
                receive_from_deepgram(),
                send_to_deepgram()
            )
            
    except WebSocketDisconnect:
        print("[CALL] Disconnected")
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        print(f"[FINAL TRANSCRIPT] {' '.join(full_transcript)}")

if __name__ == "__main__":
    print("[SERVER] Middleware server started at ws://localhost:8000/stream")
    print("[SERVER] Waiting for incoming calls...\n")
    uvicorn.run(app, host="0.0.0.0", port=8000)
