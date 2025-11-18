# Call Middleware - Phone Call Transcription System

Complete system to simulate phone calls, capture audio via WebSocket and process it with AI for real-time transcription.

## 🔄 How Does the System Work?

### System Architecture

```
┌─────────────────────┐         WebSocket          ┌──────────────────────┐
│  call_simulator.py  │ ───────────────────────────> │   middleware.py      │
│  (Client)           │    Audio streaming          │   (Server)           │
│                     │    in 3200-byte chunks      │                      │
│  - Reads sample.wav │                             │  - Receives chunks   │
│  - Sends chunks     │                             │  - Accumulates audio │
│  - Simulates call   │                             │  - Processes with AI │
└─────────────────────┘                             └──────────────────────┘
                                                              │
                                                              ▼
                                                    ┌──────────────────────┐
                                                    │   Deepgram API       │
                                                    │   (Transcription)    │
                                                    │                      │
                                                    │  - Receives audio    │
                                                    │  - Detects language  │
                                                    │  - Transcribes text  │
                                                    └──────────────────────┘
```

### Processing Flow

1. **`middleware.py`** (Server) - Starts and waits for WebSocket connections
2. **`call_simulator.py`** (Client) - Connects to server and simulates a call
3. Client reads `sample.wav` and sends it in **3200-byte chunks**
4. Server **accumulates all chunks** in a buffer
5. When call ends (WebSocket closes):
   - Server processes complete audio with **Deepgram**
   - Gets transcription, confidence and detected language
   - Displays results in console

## 📋 Requirements

- Python 3.7+
- Deepgram account (for AI transcription)

## 🔧 Installation

1. Install dependencies:
```bash
pip install deepgram-sdk python-dotenv fastapi uvicorn websockets openai
```

2. Configure Deepgram API key in `.env` file:
```env
DEEPGRAM_API_KEY=your_api_key_here
```

## 🚀 Usage

### Option 1: Complete Call Simulation System (RECOMMENDED)

This is the main project flow - simulates a real phone call:

**Step 1: Start the middleware server**
```bash
python middleware.py
```
You'll see:
```
🚀 Middleware server started at ws://localhost:8000/stream
⏳ Waiting for incoming calls...
```

**Step 2: In another terminal, run the simulator**
```bash
python call_simulator.py
```

The simulator:
- Connects to server via WebSocket
- Reads `sample.wav` and sends it in chunks (simulating live audio)
- Closes connection

The server:
- Receives all chunks
- When call ends, processes audio with Deepgram
- Displays complete transcription

**Option 2: Automated Script**
```bash
python test_call_system.py
```
This script starts both processes automatically.

## 📁 Project Files

### 🔥 Main Files (Call System)

- **`middleware.py`**: WebSocket server that receives audio and processes it with Deepgram
  - Listens on `ws://localhost:8000/stream`
  - Accumulates audio chunks
  - Transcribes when call ends
  
- **`call_simulator.py`**: Client that simulates a phone call
  - Reads `sample.wav`
  - Sends audio in chunks via WebSocket
  - Simulates real-time transmission

- **`test_call_system.py`**: Automated script that runs both processes
- **`sample.wav`**: Sample audio file (204KB)

## 🎯 Features

- ✅ Automatic language detection
- ✅ Smart text formatting
- ✅ Transcription confidence indicator
- ✅ WAV file support
- ✅ Robust error handling

## 🔄 System Flow

### Main System (Call Simulation)
```
1. Middleware server starts and waits for connections
2. Client connects via WebSocket
3. Client sends audio in 3200-byte chunks
4. Server accumulates all chunks
5. Client closes connection (end of call)
6. Server processes complete audio with Deepgram AI
7. Server displays transcription
```

## 🌐 Supported Languages

Deepgram's Nova-2 model supports multiple languages including:
- Spanish (es)
- English (en)
- And many more...

Automatic language detection is enabled by default.

## 📊 Example Output

### Middleware Server (`middleware.py`)
```
🚀 Middleware server started at ws://localhost:8000/stream
⏳ Waiting for incoming calls...

📞 Call started - Client connected
📡 Chunk received: 3200 bytes (Total: 3200 bytes)
📡 Chunk received: 3200 bytes (Total: 6400 bytes)
...
📡 Chunk received: 2768 bytes (Total: 204368 bytes)
📴 Call ended - Processing complete audio...
🤖 Sending 204368 bytes to Deepgram for transcription...

============================================================
🔊 CALL TRANSCRIPTION:
============================================================
   📝 Text: Hello. This is a robotic test for development purposes.
   ✅ Confidence: 93.16%
   🌐 Language: en
============================================================
```

### Client Simulator (`call_simulator.py`)
```
📞 Starting phone call simulation...
🔌 Connecting to middleware server...

✅ Connected to server
📁 File: sample.wav (204368 bytes)
📡 Sending audio in 3200-byte chunks...

   Chunk #1: 3200 bytes sent (Total: 3200/204368)
   Chunk #2: 3200 bytes sent (Total: 6400/204368)
   ...
   Chunk #64: 2768 bytes sent (Total: 204368/204368)

✅ Transmission completed: 64 chunks, 204368 total bytes
📴 Closing connection...
```

✅ Conectado al servidor
📁 Archivo: sample.wav (204368 bytes)
📡 Enviando audio en chunks de 3200 bytes...

   Chunk #1: 3200 bytes enviados (Total: 3200/204368)
   Chunk #2: 3200 bytes enviados (Total: 6400/204368)
   ...
   Chunk #64: 2768 bytes enviados (Total: 204368/204368)

✅ Transmisión completada: 64 chunks, 204368 bytes totales
📴 Cerrando conexión...
```

## 🛠️ Personalización

### Modificar el tamaño de chunks
## 🛠️ Customization

### Modify chunk size

In `call_simulator.py`, change the chunk size:
```python
while chunk := f.read(3200):  # Change 3200 to desired size
```

### Configure transcription options

In `middleware.py`, customize Deepgram options:
```python
response = deepgram.listen.v1.media.transcribe_file(
    request=audio_data,
    model="nova-2",           # AI model
    smart_format=True,        # Smart formatting
    detect_language=True,     # Automatic detection
    diarize=True,            # Separate by speakers
    punctuate=True,          # Add punctuation
    utterances=True,         # Split by phrases
)
```

## ❓ Frequently Asked Questions

### Which file actually processes the audio?

**`middleware.py`** is the file that processes audio with AI.

### How does the call simulation work?

1. `call_simulator.py` acts as a **phone** making a call
2. `middleware.py` acts as a **telephony server** receiving the call
3. Audio is transmitted in **real-time** (small chunks with delays)
4. When call ends, server processes all accumulated audio

### Can I use my own audio file?

Yes, simply replace `sample.wav` with your WAV file.

### Does it work with other audio formats?

Deepgram supports: WAV, MP3, MP4, FLAC, OGG, WebM, etc. Just change the filename in the scripts.

## 📝 Notes

- Audio file should be in WAV format
- Deepgram API key must have available credits
- For large files, consider using streaming instead of batch transcription
