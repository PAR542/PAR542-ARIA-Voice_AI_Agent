import requests

def call_ollama(prompt):
    url = "http://localhost:11434/api/generate"

    data = {
        "model": "phi3",
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0,
            "num_predict": 100   # 🔥 limits hallucination
        }
    }

    response = requests.post(url, json=data)

    return response.json().get("response", "").strip()