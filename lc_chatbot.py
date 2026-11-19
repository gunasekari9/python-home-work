from dotenv import load_dotenv

load_dotenv(override=True)  # first, so LangSmith settings are loaded

from pathlib import Path
from pypdf import PdfReader
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver

PDF_NAME = "data/research.pdf"

file = Path(__file__).parent / PDF_NAME

reader = PdfReader(file)


# Groq's free plan has a small token limit, so keep the text short
pdf_text = ""
for page in reader.pages:
    pdf_text += page.extract_text() or ""

pdf_text = pdf_text[:8000]

agent = create_agent(
    model="groq:openai/gpt-oss-120b",
    system_prompt=f"""
    You are a helpful assistant chatbot.

    Use only the below information to answer.
    If the answer is not in the information, say you don't know.

    {pdf_text}
    """,
    checkpointer=InMemorySaver(),
)

def invoke_chat(user_msg: str, config):

    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": user_msg
                }
            ]
        },
        config=config
    )

    return result["messages"][-1].content