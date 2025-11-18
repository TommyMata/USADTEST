# 🌐 Web Client Demo - Real-Time Streaming Transcription

## How to Run the Web Demo

### 1. Start the server

```bash
python middleware.py
```

You'll see:
```
[SERVER] Middleware server started at ws://localhost:8000/stream
[SERVER] Waiting for incoming calls...
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### 2. Open your browser

Go to: **http://localhost:8000**

### 3. Use the demo

1. Click **"🎤 Start Call"**
2. Allow microphone access when prompted
3. **Speak into your microphone** - watch the text appear in real-time!
4. Click **"⏹️ End Call"** when finished
5. See your complete transcription with confidence and language detected

---

## 📊 What You'll See

```
┌──────────────────────────────────────────────────┐
│     📞 Real-Time Call Transcription Demo         │
│                                                  │
│  Status: 🟢 Recording... Speak now!             │
│                                                  │
│  [🎤 Start Call]  [⏹️ End Call]                 │
│                                                  │
│  Transcription:                                  │
│  ┌────────────────────────────────────────────┐ │
│  │ Hello, this is a real-time transcription  │ │
│  │ demo. The text appears as I speak...      │ │
│  └────────────────────────────────────────────┘ │
│                                                  │
│  Confidence: 97.80%  Language: EN  Duration: 5s │
└──────────────────────────────────────────────────┘
```

### Real-Time Features

✨ **Interim Results** - See partial text while speaking (gray color)  
✨ **Final Results** - Complete phrases confirmed (black color)  
✨ **Live Updates** - Text appears instantly, not after you stop  
✨ **Multi-Language** - Automatically detects Spanish, English, etc.

---

## 🎯 Perfect for Client Demo

✅ **Real-Time** - Text appears as you speak, not after  
✅ **Visual** - Client sees everything happening live  
✅ **Interactive** - Immediate feedback and engagement  
✅ **Professional** - Modern gradient UI with smooth animations  
✅ **Simple** - Just click and talk, no technical knowledge needed  
✅ **Multi-Language** - Automatically detects and transcribes any language

---

## 🔧 How It Works (Technical Flow)

```
┌─────────────────┐        ┌─────────────────┐        ┌─────────────────┐
│   Browser Mic   │───────▶│  Middleware.py  │───────▶│  Deepgram API   │
│                 │  PCM   │                 │  PCM   │                 │
│  - Captures     │  Audio │  - WebSocket    │  Audio │  - Streaming    │
│  - Converts PCM │        │    Relay        │        │    Recognition  │
│                 │◀───────│                 │◀───────│                 │
│  Shows Results  │  JSON  │  Forwards       │  JSON  │  Sends Results  │
└─────────────────┘        └─────────────────┘        └─────────────────┘
```

### Step-by-Step Process:

1. **Browser captures microphone** using WebRTC MediaRecorder API
2. **Audio converted to PCM format** (16-bit, 16kHz, mono)
3. **Sent via WebSocket** to middleware.py in real-time chunks
4. **Middleware relays** audio chunks to Deepgram streaming API
5. **Deepgram processes** and returns interim + final transcriptions
6. **Middleware forwards** results back to browser
7. **Browser displays** text immediately in the UI

### Audio Format Details:
- **Encoding**: Linear PCM (uncompressed)
- **Sample Rate**: 16,000 Hz (optimal for speech)
- **Bit Depth**: 16-bit
- **Channels**: 1 (mono)
- **Chunk Size**: 4096 samples (~256ms per chunk)

---

## 📝 Requirements

- Modern browser (Chrome, Edge, Firefox, or Safari)
- Microphone access permission
- Stable internet connection (for Deepgram API)
- Python server running on localhost:8000

---

## 💡 Tips for Best Results

1. **Speak clearly** - Better pronunciation = higher confidence
2. **Reduce background noise** - Use quiet environment
3. **Stable internet** - Ensures smooth real-time processing
4. **Allow microphone** - Required for audio capture
5. **Wait for connection** - Green status indicator before speaking

---

## 🚀 Advanced Usage

### Deploy for Remote Demos

Use **ngrok** to share with clients remotely:

```bash
# Start the server
python middleware.py

# In another terminal, expose it
ngrok http 8000
```

Then share the ngrok URL (e.g., `https://abc123.ngrok.io`) with your client!

### Multiple Language Testing

The system auto-detects languages. Try speaking:
- 🇺🇸 English: "Hello, this is a test"
- 🇪🇸 Spanish: "Hola, esta es una prueba"
- 🇫🇷 French: "Bonjour, c'est un test"
- And many more supported languages!

---

## 🚀 Next Steps & Enhancements

Want to make it even better? Consider adding:

### Features
- ✨ **Language selector** - Let users choose specific language
- 💾 **Save transcriptions** - Download as TXT or export to database
- 📊 **Analytics dashboard** - Track usage, confidence scores, languages
- 🎨 **Themes** - Light/dark mode toggle
- 🔊 **Audio playback** - Record and replay conversations
- 👥 **Multi-user support** - Multiple simultaneous transcriptions
- 🔐 **Authentication** - Secure access with login

### Integrations
- 📞 **Phone integration** - Connect with Twilio for real phone calls
- 💬 **Chat interface** - Add text chat alongside voice
- 🤖 **AI responses** - Integrate ChatGPT for intelligent replies
- 📧 **Email summaries** - Send transcription reports
- 🔗 **CRM integration** - Connect to Salesforce, HubSpot, etc.

### Deployment
- ☁️ **Cloud hosting** - Deploy to AWS, Heroku, or DigitalOcean
- 🌐 **Domain name** - Professional custom domain
- 🔒 **HTTPS/SSL** - Required for production microphone access
- 📈 **Scaling** - Load balancing for multiple users
- 🐳 **Docker** - Containerize for easy deployment

---

## 🆘 Troubleshooting

### Microphone not working
- Check browser permissions (🔒 icon in address bar)
- Try different browser (Chrome recommended)
- Ensure microphone is not used by another app

### No transcription appearing
- Check console logs (F12 → Console tab)
- Verify Deepgram API key in `.env` file
- Check internet connection
- Ensure middleware server is running

### Poor transcription quality
- Reduce background noise
- Speak more clearly and slowly
- Check microphone quality
- Ensure stable internet connection

### Connection keeps dropping
- Check firewall settings
- Verify WebSocket support in network
- Try different network (corporate firewalls may block WebSockets)

---

## 📚 Documentation

- [Deepgram API Docs](https://developers.deepgram.com/)
- [WebRTC API Reference](https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [WebSocket Protocol](https://websockets.readthedocs.io/)
