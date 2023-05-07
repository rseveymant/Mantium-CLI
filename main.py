from fastapi import FastAPI, Depends, HTTPException, Request  
from fastapi.responses import HTMLResponse  
from fastapi.staticfiles import StaticFiles  
from fastapi.templating import Jinja2Templates  
from pydantic import BaseModel  
from typing import Optional  
import os  
from dotenv import load_dotenv  
from azure_gpt import create_azure_chat_completion  
from openai_gpt import create_openai_chat_completion  
from mantium_data import fetch_mantium_data  
from app import generate_response  
  
load_dotenv()  
app = FastAPI()  

app.mount("/static", StaticFiles(directory="static"), name="static")  
templates = Jinja2Templates(directory="templates")

class RequestModel(BaseModel):  
    api_type: str  
    azure_engine: Optional[str] = None  
    azure_api_key: Optional[str] = None  
    azure_api_base: Optional[str] = None  
    openai_api_key: Optional[str] = None  
    mantium_app_id: str  
    mantium_bearer_token: str  
    query: str  

  
class ResponseModel(BaseModel):  
    best_mantium_response: str  
    final_response: str  

@app.get("/", response_class=HTMLResponse)  
async def get_root(request: Request):  
    return templates.TemplateResponse("index.html", {"request": request})  

@app.post("/generate_response", response_model=ResponseModel)  
async def generate_response_endpoint(request: RequestModel):  
    if request.api_type == "azure":  
        os.environ["AZURE_OPENAI_ENGINE"] = request.azure_engine  
        os.environ["AZURE_OPENAI_API_KEY"] = request.azure_api_key  
        os.environ["AZURE_OPENAI_API_BASE"] = request.azure_api_base  
    else:  
        os.environ["OPENAI_API_KEY"] = request.openai_api_key  
  
    mantium_results = fetch_mantium_data(request.mantium_app_id, request.mantium_bearer_token, request.query)  
    if mantium_results:  
        if 'results' in mantium_results and len(mantium_results['results']) > 0:  
            mantium_answers = [result['text'] for result in mantium_results['results'][0]['results']]  
            final_response, best_mantium_response = generate_response(request.query, request.api_type, mantium_answers)  
            return {"best_mantium_response": best_mantium_response, "final_response": final_response}  
        else:  
            raise HTTPException(status_code=400, detail="There was an error fetching data from Mantium. The 'results' key is missing or empty.")  
    else:  
        raise HTTPException(status_code=400, detail="There was an error fetching data from Mantium.")  

