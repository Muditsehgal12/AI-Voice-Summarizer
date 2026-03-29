import whisper

model = whisper.load_model("base")
def transcribe_audio(file_path, language, mode):
    lang_map = {
        "English": "en",
        "Hindi": "hi",
        "Urdu": "ur"
    }

    if mode == "Translate to English":
        result = model.transcribe(file_path, task="translate")
    else:
        if language == "Auto Detect":
            result = model.transcribe(file_path)
        else:
            result = model.transcribe(file_path, language=lang_map[language])

    return result["text"]