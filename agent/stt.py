import os
from groq import Groq
from dotenv import load_dotenv

# 🔥 load .env
load_dotenv()

# 🔥 get API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("❌ GROQ_API_KEY not found in .env")

# 🔥 initialize client
client = Groq(api_key=api_key)


def transcribe_audio(file):
    try:
        response = client.audio.transcriptions.create(
            file=(file.filename, file.stream.read(), file.mimetype),
            model="whisper-large-v3"
        )
        return response.text

    except Exception as e:
        print("❌ STT ERROR:", e)
        return "Transcription failed"