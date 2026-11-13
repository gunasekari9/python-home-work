from dotenv import load_dotenv
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from pydantic import BaseModel

load_dotenv(override=True)


class ModelResponse(BaseModel):
    response: str
    confidence: float


agent = create_agent(
    model="groq:openai/gpt-oss-120b",
    system_prompt="You are a helpful assistant chatbot.",
    checkpointer=InMemorySaver(),
    response_format=ModelResponse,
)


def invoke_chat(user_msg: str, config):
    result = agent.invoke(
        {"messages": [{"role": "user", "content": user_msg}]},
        config=config,
    )
    return result["messages"][-1].content_blocks