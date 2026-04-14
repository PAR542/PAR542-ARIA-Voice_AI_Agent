from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
import time
import re

from agent.intent import detect_intent
from agent.tools import create_file
from agent.llm import call_ollama
from agent.stt import transcribe_audio

app = Flask(__name__)
CORS(app)

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

benchmarks = []


# =========================
# 🏠 UI
# =========================
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/benchmark-page")
def benchmark_page():
    return render_template("benchmark.html")


@app.route("/benchmarks")
def get_benchmarks():
    return jsonify(benchmarks)


# =========================
# 🎤 TRANSCRIBE (FIXED)
# =========================
@app.route("/transcribe", methods=["POST"])
def transcribe():
    try:
        if "audio" not in request.files:
            return jsonify({"error": "No audio file"}), 400

        file = request.files["audio"]

        print("📥 File:", file.filename)
        print("🎧 Type:", file.mimetype)

        # 🔥 DIRECT PASS (NO FILE SAVE)
        text = transcribe_audio(file)

        return jsonify({
            "status": "success",
            "text": text
        })

    except Exception as e:
        print("❌ ERROR:", e)
        return jsonify({"error": str(e)}), 500


# =========================
# 🧠 PROCESS
# =========================
@app.route("/process", methods=["POST"])
def process():
    data = request.json
    user_text = data.get("text", "").strip()

    if not user_text:
        return jsonify({"result": "No input"})

    intent_data = detect_intent(user_text)
    intent = intent_data.get("intent", "chat")
    filename = intent_data.get("filename", "")

    result = ""
    benchmark = {"time": 0, "tokens": 0}

    # CREATE FILE
    if intent == "create_file":
        filename = filename or "file.txt"
        result = create_file(filename)

    # WRITE CODE
    elif intent == "write_code":
        start = time.time()
        code = call_ollama(f"Write Python code:\n{user_text}")
        end = time.time()

        code = re.sub(r"```.*?\n", "", code).replace("```", "").strip()

        benchmark["time"] = round(end - start, 3)
        benchmark["tokens"] = len(code.split())

        filename = filename or "code.py"
        path = os.path.join(OUTPUT_DIR, filename)

        with open(path, "w") as f:
            f.write(code)

        result = f"💻 Saved: {path}"

    # CHAT
    elif intent == "chat":
        start = time.time()
        response = call_ollama(user_text)
        end = time.time()

        benchmark["time"] = round(end - start, 3)
        benchmark["tokens"] = len(response.split())

        result = response

    # SUMMARIZE
    elif intent == "summarize":
        start = time.time()
        summary = call_ollama(f"Summarize:\n{user_text}")
        end = time.time()

        benchmark["time"] = round(end - start, 3)
        benchmark["tokens"] = len(summary.split())

        result = summary

    # DEBUG
    elif intent == "debug":
        start = time.time()
        explanation = call_ollama(f"Fix this error:\n{user_text}")
        end = time.time()

        benchmark["time"] = round(end - start, 3)
        benchmark["tokens"] = len(explanation.split())

        result = explanation

    else:
        result = "No action"

    benchmarks.append({
        "input": user_text,
        "intent": intent,
        "time": benchmark["time"],
        "tokens": benchmark["tokens"]
    })

    return jsonify({
        "transcription": user_text,
        "intent": intent_data,
        "result": result,
        "benchmark": benchmark
    })


if __name__ == "__main__":
    app.run(debug=True)