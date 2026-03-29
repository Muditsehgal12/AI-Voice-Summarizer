import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import streamlit as st
from utils import transcribe_audio
import wave

# ✅ NEW IMPORT (PDF)
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Voice Summarizer", page_icon="🎤")

# ---------------- HEADER ----------------
st.title("🎤 AI Voice Note Summarizer")
st.markdown("Upload an audio file and get transcription + summary")

# ---------------- FUNCTIONS ----------------
def generate_title(text):
    return " ".join(text.split()[:6]).title()

def simple_summary(text):
    sentences = [s.strip() for s in text.split(".") if len(s.split()) > 5]
    return ". ".join(sentences[:2]) + "."

def detailed_summary(text):
    return text[:300] + "..."

def bullet_summary(text):
    sentences = [s.strip() for s in text.split(".") if len(s.split()) > 5]
    return sentences[:5]

def detect_language(text):
    text = text.lower()
    if any(w in text for w in ["the", "is", "and", "you", "we"]):
        return "English"
    return "Unknown"

def extract_keywords(text):
    return list(set(text.split()[:10]))

def get_audio_duration(file_path):
    try:
        with wave.open(file_path, 'rb') as audio:
            return round(audio.getnframes() / audio.getframerate(), 2)
    except:
        return "N/A"

# ✅ NEW FUNCTION (PDF GENERATION)
def generate_pdf(title, transcription, summary, keywords, points):
    file_path = "report.pdf"
    doc = SimpleDocTemplate(file_path)
    styles = getSampleStyleSheet()
    content = []

    content.append(Paragraph("<b>AI Voice Summary Report</b>", styles["Title"]))
    content.append(Spacer(1, 10))

    content.append(Paragraph(f"<b>Title:</b> {title}", styles["Normal"]))
    content.append(Spacer(1, 10))

    content.append(Paragraph("<b>Transcription:</b>", styles["Heading2"]))
    content.append(Paragraph(transcription, styles["Normal"]))
    content.append(Spacer(1, 10))

    content.append(Paragraph("<b>Summary:</b>", styles["Heading2"]))
    content.append(Paragraph(summary, styles["Normal"]))
    content.append(Spacer(1, 10))

    content.append(Paragraph("<b>Keywords:</b>", styles["Heading2"]))
    content.append(Paragraph(", ".join(keywords), styles["Normal"]))
    content.append(Spacer(1, 10))

    content.append(Paragraph("<b>Key Points:</b>", styles["Heading2"]))
    for p in points:
        content.append(Paragraph(f"- {p}", styles["Normal"]))

    doc.build(content)
    return file_path

# ---------------- FILE UPLOAD ----------------
uploaded_file = st.file_uploader("📤 Upload audio file", type=["mp3", "wav"])

if uploaded_file:
    st.audio(uploaded_file)
    language = st.selectbox(
    "🌍 Select Language",
    ["Auto Detect", "English", "Hindi", "Urdu"]
    )
    mode = st.radio(
        "⚙️ Mode",
        ["Transcribe", "Translate to English"]
    )

    with open("temp_audio.wav", "wb") as f:
        f.write(uploaded_file.getbuffer())
    file_path = "temp_audio.wav"

    # ---------------- TRANSCRIPTION ----------------
    with st.spinner("⏳ Converting speech to text..."):
        text = transcribe_audio(file_path, language, mode)

    if not text:
        st.error("⚠️ Transcription failed")
    else:
        st.divider()

        # ---------------- TRANSCRIPTION ----------------
        st.subheader("📝 Transcription")
        st.text_area("Text", text, height=200)

        # ---------------- INSIGHTS ----------------
        st.subheader("📊 Insights")

        col1, col2, col3 = st.columns(3)
        col1.metric("Words", len(text.split()))
        col2.metric("Language", detect_language(text))
        col3.metric("Duration", get_audio_duration(file_path))

        # ---------------- TITLE ----------------
        st.subheader("📰 Generated Title")
        title = generate_title(text)
        st.info(title)

        # ---------------- SUMMARY ----------------
        st.subheader("📌 Summary")

        mode = st.selectbox("Select Summary Type", ["Short", "Detailed"])
        summary = simple_summary(text) if mode == "Short" else detailed_summary(text)

        st.success(summary)

        # Copy-friendly
        st.code(summary)

        # ---------------- KEYWORDS ----------------
        st.subheader("🏷️ Keywords")
        keywords = extract_keywords(text)
        st.write(", ".join(keywords))

        # ---------------- KEY POINTS ----------------
        st.subheader("🔑 Key Points")
        points = bullet_summary(text)
        for point in points:
            st.write("👉", point)

        # ---------------- DOWNLOAD TEXT ----------------
        st.download_button(
            "📥 Download Summary (TXT)",
            summary,
            "summary.txt"
        )

        # ✅ NEW: DOWNLOAD PDF
        pdf_file = generate_pdf(title, text, summary, keywords, points)

        with open(pdf_file, "rb") as f:
            st.download_button(
                "📄 Download Full Report (PDF)",
                f,
                file_name="AI_Report.pdf"
            )

# ---------------- FOOTER ----------------
st.divider()
st.caption("🚀 Built using Whisper + Streamlit | By Mudit Sehgal")