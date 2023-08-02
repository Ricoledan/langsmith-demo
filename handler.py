import os
from dotenv import load_dotenv
import json
from langchain.chat_models import ChatOpenAI

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = os.getenv('LANGCHAIN_TRACING_V2')
os.environ["LANGCHAIN_ENDPOINT"] = os.getenv('LANGCHAIN_ENDPOINT')
os.environ["LANGCHAIN_API_KEY"] = os.getenv('LANGCHAIN_API_KEY')
os.environ["LANGCHAIN_PROJECT"] = os.getenv('LANGCHAIN_PROJECT')

os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')


def chat(event, context):
    llm = ChatOpenAI()

    body = {"bot": llm.predict("Tell me a fun fact about Curtis Jackson")}

    return {"statusCode": 200, "body": json.dumps(body)}
