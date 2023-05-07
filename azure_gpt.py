import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_type = "azure"
openai.api_version = "2023-03-15-preview"

def create_azure_chat_completion(engine, messages):
    openai.api_base = os.getenv("AZURE_OPENAI_API_BASE")
    openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")

    response = openai.ChatCompletion.create(
        engine=engine,
        messages=messages
    )
    return response