import os  
import requests  
from dotenv import load_dotenv  
  
load_dotenv()  
  
openai_api_key = os.getenv("OPENAI_API_KEY")  
  
def create_openai_chat_completion(engine, messages):  
    headers = {  
        "Content-Type": "application/json",  
        "Authorization": f"Bearer {openai_api_key}",  
    }  
    data = {  
        "model": engine,  
        "messages": messages,  
    }  
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)  
  
    if response.status_code != 200:  
        response.raise_for_status()  
  
    response_data = response.json()  
    return response_data  