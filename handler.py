import os
import json
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI

load_dotenv()

os.getenv('LANGCHAIN_TRACING_V2')
os.getenv('LANGCHAIN_ENDPOINT')
os.getenv('LANGCHAIN_API_KEY')
os.getenv('LANGCHAIN_PROJECT')
os.getenv('OPENAI_API_KEY')


def chat(event, context):
    llm = ChatOpenAI()
    body = {"bot": llm.predict("Tell me about NYC Drill music")}

    return {"statusCode": 200, "body": json.dumps(body)}
