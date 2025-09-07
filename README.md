# 🌦️🤖 Wello – Weather & Wellness AI Agent

Wello is a lightweight AI agent built with [LangChain](https://www.langchain.com/), [LlamaCpp](https://github.com/ggerganov/llama.cpp), and [Gradio](https://gradio.app/).  
It acts as a friendly assistant that provides real-time weather info (via [Open-Meteo](https://open-meteo.com/)) and simple wellness tips.

---

 Features
Real weather info: (currently set for Kochi, India – extendable to other cities)  
Wellness tips: based on weather conditions  
Chat interface: powered by Gradio  
Lightweight: runs locally with TinyLlama 1.1B model  

---

 Getting Started

 1. Clone the repo
git clone https://github.com/jocode21/wello-ai-agent.git
cd wello-ai-agent

2. Create a Conda environment:
conda create -n ai_agent python=3.10
conda activate ai_agent

Install dependencies:
pip install -r requirements.txt

3. Download the TinyLlama chat model (≈600MB):
hf download TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF \
tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf \
--local-dir ./models

4. Run the app
python app.py

<img width="1600" height="264" alt="image" src="https://github.com/user-attachments/assets/3abade06-e955-4516-a3d9-15b8ac9a81ac" />

<img width="1600" height="341" alt="image" src="https://github.com/user-attachments/assets/53b2cb86-c2fb-4016-91a2-fea3ff7efafc" />

