# 🎤 AI Voice Note Summarizer

An AI-powered web application that converts speech to text and generates smart summaries from audio files. Built using Whisper and Streamlit, this project allows users to upload audio and instantly get transcription, keywords, and summaries.

---

## 🌐 Live Demo
👉 https://ai-voice-summarizer-mudit.streamlit.app

---

## ✨ Features

- 🎧 Upload audio files (MP3, WAV)
- 🧠 Speech-to-text transcription using Whisper
- 📌 Multiple summary types (Short / Detailed)
- 🏷️ Keyword extraction
- 🔑 Key points generation
- 📊 Insights (word count, language, duration)
- 📄 Download summary as TXT / PDF
- 🌍 Multi-language support (English, Hindi, Urdu)
- ⚡ Clean and responsive UI

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Whisper (OpenAI)
- Transformers (Hugging Face)
- ReportLab (PDF generation)

---

## 🧠 How It Works

1. User uploads an audio file
2. Audio is processed using Whisper model
3. Transcription is generated
4. Text is analyzed to extract:
   - Summary
   - Keywords
   - Key points
5. Results are displayed and can be downloaded

---

## 📂 Project Structure
AI-Voice-Summarizer/
│
├── app.py # Main Streamlit app
├── utils.py # Transcription + logic
├── requirements.txt # Python dependencies
├── packages.txt # System dependencies (ffmpeg)
└── .streamlit/
└── config.toml


---

## ⚙️ Installation (Local Setup)

```bash
git clone https://github.com/Muditsehgal12/AI-Voice-Summarizer.git
cd AI-Voice-Summarizer

pip install -r requirements.txt
streamlit run app.py

🚀 Deployment

Deployed on Streamlit Cloud using GitHub integration.

📌 Future Improvements
🎙️ Live microphone recording
🤖 Advanced AI summarization (BART / T5)
📜 History tracking
🌗 Dark/Light mode toggle
🌐 More language support
👨‍💻 Author

Mudit Sehgal
B.Tech AI & ML Student
Chandigarh University

⭐ Show Your Support

If you like this project, give it a ⭐ on GitHub!
