import os  
import openai  
from dotenv import load_dotenv  
  
load_dotenv()  
  
openai.api_key = os.getenv("OPENAI_API_KEY")  
  
def create_openai_chat_completion(engine, messages):  
    response = openai.ChatCompletion.create(  
        model=engine,  
        messages=messages  
    )  
    return response  