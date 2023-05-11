import os
import requests
from dotenv import load_dotenv
load_dotenv()

def create_anthropic_chat_completion(engine, messages):
    anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {anthropic_api_key}"
    }
    
    data = {
        "model": engine,
        "messages": messages
    }
    
    response = requests.post("https://api.anthropic.ai/v1/chat/completions", headers=headers, json=data)
    
    if response.status_code != 200:
        response.raise_for_status()
        
    response_data = response.json()
    return response_data 
