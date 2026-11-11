import os
import base64
import requests
from dotenv import load_dotenv
import chainlit as cl
from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain.tools import tool

load_dotenv()
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

# ---- Google Search Tool ----
@tool
def google_search(query: str) -> str:
    """Search Google for current information using Serper.dev."""
    url = "https://google.serper.dev/search"
    headers = {"X-API-KEY": SERPER_API_KEY, "Content-Type": "application/json"}
    resp = requests.post(url, headers=headers, json={"q": query})
    data = resp.json()
    results = data.get("organic", [])[:3]
    if not results:
        return "No results found."
    return "\n".join(f"{r.get('title')}: {r.get('snippet')}" for r in results)

tools = [google_search]

# ---- LLM 1: Text agent (reasoning + search) ----
llm = ChatOllama(model="qwen2.5", temperature=0.5)

SYSTEM_PROMPT = (
    "You are Om's Chatbot, a helpful assistant. Give clear, well-formatted, "
    "multiline answers when the question needs detail. Use the google_search "
    "tool whenever the user asks about current events, prices, or anything "
    "you might not know."
)

agent_executor = create_agent(model=llm, tools=tools, system_prompt=SYSTEM_PROMPT)

# ---- LLM 2: Vision model (image understanding/summary) ----
vision_llm = ChatOllama(model="llama3.2-vision")

chat_history = []

@cl.on_chat_start
async def start():
    await cl.Message(
        content="👋 Hi, I'm **Om's Chatbot**. Ask me anything, or upload an image for a summary!"
    ).send()

@cl.on_message
async def main(message: cl.Message):
    images = [el for el in message.elements if "image" in el.mime]

    if images:
        img_path = images[0].path
        with open(img_path, "rb") as f:
            img_b64 = base64.b64encode(f.read()).decode("utf-8")

        response = vision_llm.invoke([
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": message.content or "Summarize this image in detail."},
                    {
                        "type": "image",
                        "source_type": "base64",
                        "data": img_b64,
                        "mime_type": images[0].mime,
                    },
                ],
            }
        ])
        await cl.Message(content=response.content).send()
        return

    chat_history.append({"role": "user", "content": message.content})
    result = agent_executor.invoke({"messages": chat_history})
    answer = result["messages"][-1].content
    chat_history.append({"role": "assistant", "content": answer})
    await cl.Message(content=answer).send()