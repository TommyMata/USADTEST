# 🌐 Web Client Demo - Quick Start

## How to Run the Web Demo

### 1. Start the server

```bash
python middleware.py
```

You'll see:
```
[SERVER] Middleware server started at ws://localhost:8000/stream
[SERVER] Waiting for incoming calls...
```

### 2. Open your browser

Go to: **http://localhost:8000**

### 3. Use the demo

1. Click **"🎤 Start Call"**
2. Allow microphone access
3. **Speak** into your microphone
4. Click **"⏹️ End Call"**
5. Wait 2-3 seconds
6. See your **transcription**!

---

## 📊 What You'll See

```
┌─────────────────────────────────────┐
│ 📞 Call Transcription Demo          │
│                                     │
│ Status: Recording...  [YELLOW]      │
│                                     │
│ [🎤 Start Call]  [⏹️ End Call]     │
│                                     │
│ Transcription:                      │
│ ┌─────────────────────────────────┐ │
│ │ Hello. This is a test call...   │ │
│ └─────────────────────────────────┘ │
│                                     │
│ Confidence: 94.2%  Language: EN    │
└─────────────────────────────────────┘
```

---

## 🎯 Perfect for Client Demo

✅ **Visual** - Client sees everything happening  
✅ **Interactive** - Real-time experience  
✅ **Professional** - Modern UI  
✅ **Simple** - Just click and talk  

---

## 🔧 How It Works

```
Browser Mic → WebSocket → Middleware → Deepgram → Transcription
```

1. Browser captures audio from microphone
2. Sends chunks via WebSocket (same as call_simulator.py)
3. Middleware accumulates audio
4. Sends to Deepgram AI
5. Returns transcription to display

---

## 📝 Notes

- Works with Chrome, Edge, Firefox
- Requires microphone permission
- Same backend as your current system
- No installation needed for client
- Can share via ngrok for remote demos

---

## 🚀 Next Steps

Want to make it better? You can:

- Add real-time transcription (while speaking)
- Add multiple language support selector
- Save transcription history
- Add authentication
- Deploy to cloud (Heroku, AWS, etc.)
