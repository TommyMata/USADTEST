# Call Middleware - Real-Time Phone Call Transcription System

Complete system for real-time audio transcription using AI. Features **streaming transcription** that displays text as you speak, with support for browser-based WebRTC calls and simulated phone calls.

## 🔄 How Does the System Work?

### System Architecture (Real-Time Streaming)

```
┌──────────────────────┐       WebSocket        ┌──────────────────────┐       WebSocket       ┌──────────────────────┐
│  web_client.html     │ ◄──────────────────────►│   middleware.py      │◄─────────────────────►│   Deepgram API       │
│  (Browser)           │   Audio PCM chunks      │   (Server)           │   Streaming audio     │   (Live Streaming)   │
│                      │   + Real-time results   │                      │   + Live transcripts  │                      │
│  - Captures mic      │                         │  - Relays audio      │                       │  - Speech-to-text    │
│  - Sends PCM audio   │                         │  - Forwards results  │                       │  - Interim results   │
│  - Shows transcript  │                         │  - Bridges WebSockets│                       │  - Final results     │
└──────────────────────┘                         └──────────────────────┘                       └──────────────────────┘
                                                            ▲
                                                            │
                                                            │ WebSocket (alternative)
                                                            │
                                                  ┌──────────────────────┐
                                                  │  call_simulator.py   │
                                                  │  (CLI Client)        │
                                                  │                      │
                                                  │  - Reads sample.wav  │
                                                  │  - Sends chunks      │
                                                  │  - Simulates call    │
                                                  └──────────────────────┘
```

### Processing Flow (Streaming Mode)

1. **Browser/Client** connects to `middleware.py` via WebSocket
2. **Audio capture** begins (microphone or file)
3. Audio is sent in **real-time chunks** (PCM 16-bit, 16kHz)
4. **Middleware** relays chunks to **Deepgram streaming API**
5. **Deepgram** returns:
   - **Interim results** (partial transcription while speaking)
   - **Final results** (complete phrases)
6. **Results appear in real-time** on web interface

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

### Option 1: Web Browser Demo (RECOMMENDED - Real-Time Streaming)

The easiest way to see real-time transcription in action:

**Step 1: Start the server**
```bash
python middleware.py
```

**Step 2: Open your browser**
Go to: **http://localhost:8000**

**Step 3: Use the demo**
1. Click **"Start Call"**
2. Allow microphone access
3. **Speak** - see text appear in real-time!
4. Click **"End Call"**

### Option 2: Command-Line Call Simulation

For testing with audio files:

**Step 1: Start the middleware server**
```bash
python middleware.py
```

**Step 2: In another terminal, run the simulator**
```bash
python call_simulator.py
```

**Option 3: Automated Script**
```bash
python test_call_system.py
```

## 📁 Project Files

### 🔥 Main Files

- **`middleware.py`**: WebSocket server with streaming transcription
  - Serves web client at `http://localhost:8000`
  - Relays audio to Deepgram streaming API
  - Forwards real-time transcriptions to browser
  
- **`web_client.html`**: Browser-based WebRTC interface
  - Captures microphone audio
  - Converts to PCM format
  - Displays transcriptions in real-time
  - Shows interim and final results

- **`call_simulator.py`**: CLI client for testing with audio files
  - Reads `sample.wav`
  - Sends audio chunks via WebSocket
  - Simulates phone call transmission

- **`test_call_system.py`**: Automated testing script
- **`sample.wav`**: Sample audio file for testing (204KB)
- **`WEB_DEMO.md`**: Web client documentation

## 🎯 Features

- ✅ **Real-time streaming transcription** - See text as you speak
- ✅ **Interim results** - Partial transcriptions while speaking
- ✅ **Final results** - Complete phrases with high accuracy
- ✅ **Automatic language detection** - Spanish, English, and more
- ✅ **Browser-based interface** - No installation needed
- ✅ **Smart text formatting** - Proper punctuation and capitalization
- ✅ **Confidence indicators** - Know transcription reliability
- ✅ **Multi-language support** - Speak in any supported language
- ✅ **WebRTC audio capture** - Professional-grade microphone processing
- ✅ **Robust error handling** - Graceful connection management

## 🔄 System Flow

### Web Browser Flow (Real-Time Streaming)
```
1. User opens http://localhost:8000 in browser
2. Clicks "Start Call" and allows microphone access
3. Browser captures audio and converts to PCM format
4. Audio chunks sent to middleware via WebSocket
5. Middleware forwards chunks to Deepgram streaming API
6. Deepgram sends back interim transcriptions (while speaking)
7. Deepgram sends final transcriptions (complete phrases)
8. Middleware relays results to browser in real-time
9. User sees text appearing as they speak
10. Click "End Call" to finish
```

### CLI Simulation Flow
```
1. Middleware server starts and waits for connections
2. call_simulator.py connects via WebSocket
3. Simulator sends audio file in chunks
4. Middleware relays to Deepgram streaming
5. Transcriptions printed to console
6. Connection closes when file complete
```

## 🌐 Supported Languages

Deepgram's Nova-2 model supports multiple languages including:
- Spanish (es)
- English (en)
- And many more...

Automatic language detection is enabled by default.

## 📊 Example Output

### Web Browser Interface
```
┌─────────────────────────────────────────────────────┐
│        📞 Real-Time Call Transcription Demo         │
├─────────────────────────────────────────────────────┤
│                                                     │
│  Status: 🟢 Recording... Speak now!                │
│                                                     │
│  [🎤 Start Call]  [⏹️ End Call]                    │
│                                                     │
│  Transcription:                                     │
│  ┌───────────────────────────────────────────────┐ │
│  │ Hello, this is a real-time transcription     │ │
│  │ demo using AI. The text appears as I speak.  │ │
│  └───────────────────────────────────────────────┘ │
│                                                     │
│  Confidence: 97.80%    Language: EN    Duration: 8s│
│                                                     │
└─────────────────────────────────────────────────────┘
```

### Middleware Server Console (`middleware.py`)
```
[SERVER] Middleware server started at ws://localhost:8000/stream
[SERVER] Waiting for incoming calls...

INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     127.0.0.1:52189 - "WebSocket /stream" [accepted]
[CALL] Started - Client connected
[DEEPGRAM] Connected to streaming API

[TRANSCRIPT] [INTERIM] Hello, this
[TRANSCRIPT] [FINAL] Hello, this is a real-time
[TRANSCRIPT] [INTERIM] transcription demo
[TRANSCRIPT] [FINAL] transcription demo using AI.
[TRANSCRIPT] [INTERIM] The text appears
[TRANSCRIPT] [FINAL] The text appears as I speak.

[CALL] Ended
[FINAL TRANSCRIPT] Hello, this is a real-time transcription demo using AI. The text appears as I speak.
```

## 🛠️ Customization

### Configure streaming options

In `middleware.py`, modify the Deepgram WebSocket URL:
```python
deepgram_url = f"wss://api.deepgram.com/v1/listen?" \
               f"model=nova-2&" \           # AI model
               f"language=multi&" \          # Auto-detect or specify (en, es, etc.)
               f"smart_format=true&" \       # Smart formatting
               f"interim_results=true&" \    # Show partial results
               f"punctuate=true&" \          # Add punctuation
               f"encoding=linear16&" \       # PCM format
               f"sample_rate=16000"          # Audio sample rate
```

### Modify audio capture settings

In `web_client.html`, adjust microphone settings:
```javascript
const stream = await navigator.mediaDevices.getUserMedia({ 
    audio: {
        channelCount: 1,      // Mono audio
        sampleRate: 16000     // 16kHz (Deepgram optimized)
    }
});
```

### Change chunk size for CLI simulator

In `call_simulator.py`:
```python
while chunk := f.read(3200):  # Change 3200 to desired size
```

## ❓ Frequently Asked Questions

### How does real-time streaming work?

Instead of waiting for the entire call to finish, audio is sent to Deepgram's streaming API in small chunks. Deepgram processes audio continuously and returns:
- **Interim results**: Partial transcriptions (temporary)
- **Final results**: Complete phrases (permanent)

### What's the difference between interim and final results?

- **Interim**: Appear while you're still speaking (gray text in browser)
- **Final**: Confirmed complete phrases (black text in browser)

### Can I use this for actual phone calls?

Yes! You could integrate with:
- **FreeSWITCH** or **Kamailio** for SIP calls
- **Twilio** for phone number integration
- **WebRTC** for browser-to-browser calls (already implemented)

### Which browsers are supported?

- ✅ Chrome/Edge (Recommended)
- ✅ Firefox
- ✅ Safari (with permissions)

### Can I use my own audio file?

Yes, use `call_simulator.py` and replace `sample.wav` with your file.

### Does it work with other audio formats?

The browser interface requires PCM audio. The CLI simulator supports any format Deepgram accepts (WAV, MP3, FLAC, etc.)

## 📝 Notes

- **Real-time transcription** requires stable internet connection
- **Deepgram API** must have available credits
- **Browser microphone** requires HTTPS in production (works on localhost)
- **Interim results** may change before final confirmation
- **Audio format**: PCM 16-bit, 16kHz, mono channel
- **Latency**: Typically 200-500ms from speech to text
- **Supported languages**: See [Deepgram documentation](https://developers.deepgram.com/docs/languages)
