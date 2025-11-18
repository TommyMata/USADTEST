import os
import io
from fastapi import FastAPI, WebSocket
import uvicorn
from starlette.websockets import WebSocketDisconnect
from dotenv import load_dotenv
from deepgram import DeepgramClient

load_dotenv()

app = FastAPI()
API_KEY = os.getenv("DEEPGRAM_API_KEY")

@app.websocket("/stream")
async def audio_stream(ws: WebSocket):
    await ws.accept()
    print("[CALL] Started - Client connected")
    
    # Buffer to accumulate audio chunks
    audio_buffer = io.BytesIO()
    total_bytes = 0
    
    try:
        while True:
            data = await ws.receive_bytes()
            total_bytes += len(data)
            audio_buffer.write(data)
            print(f"[CHUNK] Received: {len(data)} bytes (Total: {total_bytes} bytes)")
            
    except WebSocketDisconnect:
        print("[CALL] Ended - Processing complete audio...")
        
        # Process all accumulated audio with Deepgram
        if total_bytes > 0:
            try:
                deepgram = DeepgramClient(api_key=API_KEY)
                audio_data = audio_buffer.getvalue()
                
                print(f"[AI] Sending {total_bytes} bytes to Deepgram for transcription...")
                
                response = deepgram.listen.v1.media.transcribe_file(
                    request=audio_data,
                    model="nova-2",
                    smart_format=True,
                    detect_language=True
                )
                
                transcript = response.results.channels[0].alternatives[0].transcript
                confidence = response.results.channels[0].alternatives[0].confidence
                detected_language = response.results.channels[0].detected_language if hasattr(response.results.channels[0], 'detected_language') else "Not detected"
                
                print("\n" + "="*60)
                print("CALL TRANSCRIPTION:")
                print("="*60)
                print(f"   Text: {transcript}")
                print(f"   Confidence: {confidence:.2%}")
                print(f"   Language: {detected_language}")
                print("="*60 + "\n")
                
            except Exception as e:
                print(f"[ERROR] Transcription error: {e}")
        else:
            print("[WARNING] No audio received to process")

if __name__ == "__main__":
    print("[SERVER] Middleware server started at ws://localhost:8000/stream")
    print("[SERVER] Waiting for incoming calls...\n")
    uvicorn.run(app, host="0.0.0.0", port=8000)
