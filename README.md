# 🎬 Instagram Reel Transcriber

[![Live Demo](https://img.shields.io/badge/Live_Demo-Streamlit_Cloud-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://insta-reel-transcriber.streamlit.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)

> **Extract text from any Instagram Reel in seconds.** Powered by OpenAI's Whisper AI.

## ✨ Live Demo

👉 **[insta-reel-transcriber.streamlit.app](https://insta-reel-transcriber.streamlit.app/)** 👈

Paste a URL, click transcribe, get your transcript. No downloads. No clutter.

---

## 📸 Demo
┌─────────────────────────────────────────────────────────────┐
│ │
│ 🔗 [https://www.instagram.com/reel/xxxxx] │
│ │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ [ TRANSCRIBE ] │ │
│ └─────────────────────────────────────────────────────┘ │
│ │
│ ✨ Transcription complete! │
│ │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ "This is the transcribed text from your reel..." │ │
│ │ │ │
│ └─────────────────────────────────────────────────────┘ │
│ │
└─────────────────────────────────────────────────────────────┘

text

---

## 🚀 Features

| Feature | Description |
|---------|-------------|
| 🎯 **One-Click** | Paste URL → Get transcript |
| 🗑️ **Auto-Cleanup** | Videos deleted immediately after processing |
| 🔒 **Privacy First** | No storage, no tracking, no credentials |
| 🌐 **Works Anywhere** | Desktop, tablet, phone |
| ⚡ **Fast** | Powered by Whisper AI |
| 🆓 **Completely Free** | No paywalls, no signup |

---

## 🛠️ Tech Stack
┌─────────────────────────────────────────────────────────────┐
│ │
│ Instagram URL ──► yt-dlp ──► Whisper AI ──► Transcript │
│ │ │ │
│ ▼ ▼ │
│ Downloads OpenAI's │
│ Reel ASR Model │
│ │ │ │
│ └─────┬──────┘ │
│ ▼ │
│ Auto-Delete ✅ │
│ │
└─────────────────────────────────────────────────────────────┘

text

| Technology | Purpose |
|------------|---------|
| **[Streamlit](https://streamlit.io/)** | Web interface |
| **[yt-dlp](https://github.com/yt-dlp/yt-dlp)** | Instagram Reel downloader |
| **[OpenAI Whisper](https://openai.com/research/whisper)** | Speech-to-text AI |
| **[PyTorch](https://pytorch.org/)** | ML framework |

---

## 📦 Local Setup

### Prerequisites

- Python 3.11 or higher
- pip
- ffmpeg

### Installation

```bash
# Clone the repo
git clone https://github.com/VisheshD2412/insta-reel-transcriber.git
cd insta-reel-transcriber

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install ffmpeg (required for audio processing)
# macOS:
brew install ffmpeg
# Ubuntu/Debian:
sudo apt update && sudo apt install ffmpeg
# Windows:
# Download from https://ffmpeg.org/download.html

# Run the app
streamlit run app.py
Your app will open at http://localhost:8502

☁️ Deployment
This app is deployed on Streamlit Community Cloud.

Deploy your own fork:
Fork this repository

Go to share.streamlit.io

Connect your GitHub account

Select your fork

Click "Deploy"

📁 Project Structure
text
insta-reel-transcriber/
├── app.py                 # Main application
├── requirements.txt       # Python dependencies
├── packages.txt          # System dependencies (ffmpeg)
├── runtime.txt           # Python version (3.11)
├── LICENSE               # MIT License
└── README.md            # This file
🔧 Environment Variables
None required! This app runs without any API keys or configuration.

🧪 Usage Examples
Valid URL format:

text
https://www.instagram.com/reel/[REEL_ID]/
Tips:

✅ Works with public reels only

✅ Supports any language

✅ No login required

✅ No rate limits (within reason)

📊 Performance
Metric	Value
Download Speed	~5-10 MB/s
Transcription	~10-30 seconds
File Cleanup	Immediate
Model Size	~1.4 GB (first run)
🛡️ Privacy & Security
Concern	How it's handled
Data Storage	❌ None - videos deleted immediately
Tracking	❌ No analytics or tracking
Credentials	❌ Never requested
Logging	❌ No user data logged
Encryption	✅ HTTPS for all requests
🐛 Troubleshooting
Issue	Solution
ModuleNotFoundError	Run pip install -r requirements.txt
ffmpeg not found	Install ffmpeg (see Local Setup)
"Private reel" error	Reel must be public
Slow first run	Whisper model downloads first time
App won't load	Hard refresh (Cmd+Shift+R / Ctrl+Shift+R)
🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first.

bash
# Fork the repo
# Then:
git checkout -b feature/amazing-feature
git commit -m 'Add amazing feature'
git push origin feature/amazing-feature
# Open a Pull Request
📄 License
Distributed under the MIT License. See LICENSE for more information.

🙏 Acknowledgments
OpenAI Whisper - Speech recognition

yt-dlp - Video downloading

Streamlit - Web framework

⚠️ Disclaimer
This project is for educational purposes only. Respect Instagram's Terms of Service and content creators' rights. Do not use for copyright violation or privacy infringement.

📬 Contact
Vishesh Dalwal - @VisheshD2412

Project Link: https://github.com/VisheshD2412/insta-reel-transcriber

Live Demo: https://insta-reel-transcriber.streamlit.app/

<p align="center"> <b>⭐ Star this repo if you found it useful! ⭐</b> </p> ```
Just copy and paste this into your README.md file:
bash
# Replace your current README
cd /Users/visheshdalwal/Documents/insta-reel-transcriber

# Open README.md (or create it)
nano README.md

# Paste the entire content above
# Save (Ctrl+O, then Enter, then Ctrl+X)

# Commit and push
git add README.md
git commit -m "Add elite GitHub README with badges and live demo link"
git push origin main
