import asyncio
import websockets
import os

async def simulate_call():
    print("[CLIENT] Starting phone call simulation...")
    print("[CLIENT] Connecting to middleware server...\n")
    
    try:
        async with websockets.connect("ws://localhost:8000/stream") as ws:
            print("[CLIENT] Connected to server")
            
            # Verify that file exists
            if not os.path.exists("sample.wav"):
                print("[ERROR] sample.wav file not found")
                return
            
            file_size = os.path.getsize("sample.wav")
            print(f"[FILE] sample.wav ({file_size} bytes)")
            print("[STREAM] Sending audio in 3200-byte chunks...\n")
            
            chunks_sent = 0
            bytes_sent = 0
            
            with open("sample.wav", "rb") as f:
                while chunk := f.read(3200):
                    await ws.send(chunk)
                    chunks_sent += 1
                    bytes_sent += len(chunk)
                    print(f"   Chunk #{chunks_sent}: {len(chunk)} bytes sent (Total: {bytes_sent}/{file_size})")
                    await asyncio.sleep(0.1)  # Simulate real-time streaming
            
            print(f"\n[SUCCESS] Transmission completed: {chunks_sent} chunks, {bytes_sent} total bytes")
            print("[CLIENT] Closing connection...\n")
            
    except ConnectionRefusedError:
        print("[ERROR] Could not connect to server")
        print("[INFO] Make sure the middleware is running: python middleware.py")
    except Exception as e:
        print(f"[ERROR] Error during simulation: {e}")

if __name__ == "__main__":
    asyncio.run(simulate_call())
