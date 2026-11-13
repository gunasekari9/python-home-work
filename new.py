import os
from dotenv import load_dotenv
from groq import Groq
import groq

load_dotenv(override=True)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

conversation = {}


def chatbot(user_input: str, user_id: str = "default") -> str:
    if user_id not in conversation:
        conversation[user_id] = []

    history = conversation[user_id]

    history.append({"role": "user", "content": user_input})
    del history[:-10]  # keep only the last 10 message

    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=history,
            max_tokens=1000
        )
        res = response.choices[0].message.content
        history.append({"role": "assistant", "content": res})
        return res
    except groq.GroqError as e:
        history.pop()
        return f"ERROR: {e}"