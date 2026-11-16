from fastapi import FastAPI
from pydantic import BaseModel

from lc_chatbot import invoke_chat

app = FastAPI()


class ChatbotRequest(BaseModel):
    message: str
    thread_id: str = "default"


class ChatbotResponse(BaseModel):
    response: str
    thread_id: str


@app.post('/my-chatbot')
def my_chat_bot(request: ChatbotRequest):

    thread_id = request.thread_id or "default"

    config = {"configurable": {"thread_id": thread_id}}

    response = invoke_chat(request.message, config)

    return ChatbotResponse(response=response, thread_id=thread_id)