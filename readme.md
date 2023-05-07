# AI Assistant with FastAPI, Azure OpenAI, Mantium, and OpenAI GPT-3  
  
This AI Assistant application is built using FastAPI and integrates with Azure OpenAI, Mantium, and OpenAI GPT-3 to generate responses based on user input. The application combines the responses from Mantium and the chosen AI engine (Azure OpenAI or OpenAI GPT-3) to provide the best possible answer.  
  
## Features  
  
- FastAPI for API and web interface  
- Integration with Azure OpenAI and OpenAI GPT-3  
- Fetches data from Mantium  
- Combines responses from Mantium and the AI engine  
- Front-end interface to interact with the AI Assistant  
  
## Installation  
  
1. Clone the repository:  `git clone https://github.com/yourusername/ai-assistant.git`
`cd ai-assistant`
1. Create a virtual environment and activate it: `python3 -m venv venv`
`source venv/bin/activate`
1. Install the required packages:  `pip install -r requirements.txt`
1. Create a `.env` file in the root directory of the project and add the following variables:  
- `API_TYPE`: Either `openai` or `azure`
- `MANTIUM_APP_ID`: Mantium app ID - you can find this from a deployed plugin
- `MANTIUM_BEARER_TOKEN`: Your Mantium Bearer Token
- `OPENAI_API_KEY`: Your OpenAI API key (if using OpenAI).
- `AZURE_OPENAI_API_KEY`: Your Azure OpenAI key (if using Azure OpenAI).
- `AZURE_OPENAI_ENGINE`: The name of the Azure OpenAI engine (e.g., "gpt-3.5-turbo").
- `AZURE_OPENAI_API_BASE`: Base URL for the Azure OpenAI API

Replace the placeholders with your actual API keys and credentials.  

1. Run the FastAPI server:  `uvicorn main:app --reload`
1. Open your browser and navigate to `http://127.0.0.1:8000/` to access the AI Assistant web interface.

## Usage  
  
1. Select the API type (Azure or OpenAI) from the dropdown menu.  
2. Fill in the required API keys and credentials for the selected API type and Mantium.  
3. Enter your question in the "Your Question" field.  
4. Click "Submit" to generate a response.  
5. The best response from Mantium and the final response from the AI Assistant will be displayed on the screen.  
  
## License  
  
This project is licensed under the MIT License.  