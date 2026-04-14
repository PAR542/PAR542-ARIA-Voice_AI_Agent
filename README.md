<<<<<<< HEAD
# ARIA-Voice_AI_Agent
A voice-driven AI assistant that converts speech into structured intent and executes intelligent actions using LLMs.
=======
# 🎙️ARIA - Voice AI Agent

A modular, voice-driven AI assistant that converts speech into structured intent and executes intelligent actions using large language models.

---

## Overview

Voice AI Agent is a full-stack system that integrates speech recognition, intent classification, and LLM-powered execution into a unified interface.
It enables users to interact with an AI system using natural voice or text commands, with support for multiple task-oriented modes.

---

## Key Features

* **Voice-First Interaction**

  * Audio upload and speech-to-text processing using Groq Whisper

* **Intent-Driven Architecture**

  * Structured JSON-based intent detection
  * Reliable parsing and fallback handling

* **Multi-Mode AI Capabilities**

  * Chat (general assistant)
  * Summarization
  * Code generation
  * Debugging assistance
  * File creation

* **Execution Pipeline**

  * Input → Intent → Action → Output

* **Benchmarking System**

  * Tracks response latency and token usage
  * Dedicated dashboard for performance insights

* **Modern Interface**

  * Chat-style UI with emphasis on usability and clarity

---

## System Architecture

```
User Input (Voice / Text)
        ↓
Speech-to-Text (Groq Whisper)
        ↓
Intent Detection (LLM → JSON)
        ↓
Action Dispatcher (Flask Backend)
        ↓
LLM Processing / File System
        ↓
Response + Benchmark Metrics
```

---

## Tech Stack

| Layer     | Technology            |
| --------- | --------------------- |
| Frontend  | HTML, CSS, JavaScript |
| Backend   | Flask (Python)        |
| LLM       | Ollama / Groq         |
| STT       | Groq Whisper API      |
| Utilities | dotenv, REST APIs     |

---

## Project Structure

```
voice-ai-agent/
│
├── app.py
├── agent/
│   ├── intent.py
│   ├── stt.py
│   ├── tools.py
│   ├── llm.py
│
├── templates/
│   ├── index.html
│   ├── benchmark.html
│
├── static/
├── output/
├── temp/
├── .env
├── .gitignore
└── README.md
```

---

## Setup

### 1. Clone repository

```
git clone https://github.com/your-username/voice-ai-agent.git
cd voice-ai-agent
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_api_key_here
```

---

### 5. Run the application

```
python app.py
```

Open in browser:

```
http://127.0.0.1:5000/
```

---

## Benchmark Dashboard

Access:

```
http://127.0.0.1:5000/benchmark-page
```

Metrics include:

* Response time
* Token usage
* Request history

---

## Example Use Cases

* Create files via voice commands
* Generate and save Python scripts
* Summarize large text inputs
* Debug error messages
* General conversational queries

---

## Design Principles

* **Modularity** — clear separation between STT, intent, and execution
* **Reliability** — structured JSON outputs with fallback handling
* **Extensibility** — easy to add new intents and tools
* **Performance Awareness** — built-in benchmarking

---

## Future Enhancements

* Real-time microphone streaming
* Context-aware conversational memory
* Text-to-speech responses
* Cloud deployment and scaling

---

## License

MIT License

---

## Author

**Parv Satra**
>>>>>>> 458a1c0 (Final version)
