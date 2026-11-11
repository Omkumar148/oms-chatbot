<div align="center">

# 🤖 Om's Chatbot

**A ChatGPT-style AI assistant — built with LangChain + Ollama, fully open-source and self-hosted.**

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![LangChain](https://img.shields.io/badge/LangChain-1.4-green)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-black)
![Chainlit](https://img.shields.io/badge/UI-Chainlit-ff4785)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

</div>

---

## ✨ Features

- 💬 **Multiline, detailed answers** — not just one-liners
- 🖼️ **Image understanding** — upload any image and get a full summary
- 🔎 **Live Google search** — answers current-event and fact questions in real time
- 🧠 **Two local LLMs working together** — a reasoning/text model + a vision model
- 🆓 **100% free & open-source stack** — no paid API keys required
- 🌐 **Deployable with a free HTTPS link** — usable from any device, anywhere

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| LLM Engine | [Ollama](https://ollama.com) (qwen2.5 + llama3.2-vision) |
| Orchestration | [LangChain](https://langchain.com) |
| UI | [Chainlit](https://chainlit.io) |
| Search Tool | [Serper.dev](https://serper.dev) (Google Search API) |
| Hosting | Oracle Cloud Free Tier + Caddy (auto HTTPS) |

## 🚀 Getting Started

```bash
git clone https://github.com/YOUR_USERNAME/oms-chatbot.git
cd oms-chatbot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

ollama pull qwen2.5
ollama pull llama3.2-vision

echo "SERPER_API_KEY=your_key_here" > .env

chainlit run app.py -w
```

Open `http://localhost:8000` 🎉

## 📸 Preview

*(Add a screenshot or GIF of your chat UI here once it's running — drag it into this README on GitHub.)*

## 📄 License

MIT — free to use and modify.