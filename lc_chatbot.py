from dotenv import load_dotenv

load_dotenv(override=True)  # first, so LangSmith settings are loaded

from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver


agent = create_agent(
    model="groq:openai/gpt-oss-120b",
    system_prompt="You are a helpful assistant chatbot.",
    checkpointer=InMemorySaver(),
)


def invoke_chat(user_msg: str, config):

    result = agent.invoke(
        {
            "messages" : [
                {
                    "role" : "user",
                    "content" : user_msg
                }
            ]
        },
        config=config
    )

    return result["messages"][-1].content