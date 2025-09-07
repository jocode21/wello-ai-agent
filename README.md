# My AI Agent

A simple free AI agent built with Python, LangChain, Chroma, and local LLaMA (via llama.cpp).

## Features
- Local/offline LLM support (llama.cpp / llama-cpp-python)
- Embeddings with sentence-transformers (all-MiniLM-L6-v2)
- Memory via Chroma DB
- Basic tool integration (example: weather API)
- Gradio web UI + FastAPI backend

## Quickstart

```bash
git clone <your-repo-url>
cd my_ai_agent
python -m venv venv
source venv/bin/activate   # (Windows: .\venv\Scripts\activate)
pip install -r requirements.txt
```

Download a GGUF quantized LLaMA or other model into `models/`.

Run the app:
```bash
python app.py
```

---
