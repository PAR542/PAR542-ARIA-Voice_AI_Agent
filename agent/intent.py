import json
import re
from agent.llm import call_ollama


def extract_json(text):
    """
    Extract JSON safely from LLM response
    """
    match = re.search(r'\{.*\}', text, re.DOTALL)
    return match.group() if match else None


def detect_intent(user_input):
    """
    Detect intent using strict prompt + safe parsing
    """

    prompt = f"""
You are a strict JSON API.

Your job:
Convert user input into structured JSON.

AVAILABLE INTENTS:
- create_file
- write_code
- debug
- summarize
- run_code
- chat

RULES:
- ONLY return JSON
- NO explanation
- NO markdown
- ALWAYS include both fields
- filename MUST be string ("" if none)

FORMAT:
{{"intent":"<intent>","filename":""}}

EXAMPLES:

Input: create a file named test.txt
Output: {{"intent":"create_file","filename":"test.txt"}}

Input: write python code for sorting
Output: {{"intent":"write_code","filename":""}}

Input: run sorting.py
Output: {{"intent":"run_code","filename":"sorting.py"}}

Input: I have error index out of range
Output: {{"intent":"debug","filename":""}}

NOW PROCESS:

Input: {user_input}
Output:
"""

    try:
        response = call_ollama(prompt).strip()

        json_str = extract_json(response)

        if json_str:
            data = json.loads(json_str)

            # ✅ SAFETY FIXES
            if not isinstance(data, dict):
                raise ValueError("Invalid JSON")

            intent = data.get("intent", "chat")
            filename = data.get("filename", "")

            # ensure types
            if not isinstance(intent, str):
                intent = "chat"
            if not isinstance(filename, str):
                filename = ""

            return {
                "intent": intent.strip(),
                "filename": filename.strip()
            }

    except Exception as e:
        print("⚠️ Intent error:", e)

    # 🔥 FAILSAFE
    return {
        "intent": "chat",
        "filename": ""
    }