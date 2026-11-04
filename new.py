import os
from dotenv import load_dotenv
from groq import Groq
import groq

load_dotenv(override=True)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

history = []

print("Chatbot started. Type 'stop' to exit.")

while True:
    user_input = input("User: ").strip()

    if user_input == "":
        continue

    if user_input.lower() == "stop":
        print("Exiting here.......")
        break

    history.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=history
        )
        res = response.choices[0].message.content
        print("AI:", res)
        history.append({"role": "assistant", "content": res})
    except groq.GroqError as e:
        print("ERROR:", e)
        history.pop()