from groq import Groq
import os

from dotenv import load_dotenv


load_dotenv()


key = os.getenv("GROQ_API_KEY")

client = Groq(
    api_key = key
)

conversation = {}

def chatbot(user_input, user_id):

    if user_id not in conversation:
        conversation[user_id] = []

    history = conversation[user_id]

    history.append({
        "role" : "user",
        "content" : user_input
    })

    response = client.chat.completions.create(
        model = 'openai/gpt-oss-120b',
        messages = history
    )

    res = response.choices[0].message.content

    history.append({
        "role" : "assistant",
        "content" : res
    })

    # print(conversation)


    return res