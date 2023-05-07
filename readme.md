# MantiumCLI2

A Python script to use Mantium, Azure OpenAI, and OpenAI APIs together to generate responses based on user input.

## Setup

1. Clone this repository.
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment: `source venv/bin/activate` (Linux/macOS) or `venv\Scripts\activate` (Windows)
4. Install the required packages: `pip install -r requirements.txt`
5. Create a `.env` file with the required environment variables (see `.env.sample` for an example).
6. Run the script: `python app.py`

## Configuration

You can configure the script using the following environment variables in the `.env` file:

- `API_TYPE`: Either `openai` or `azure`
- `MANTIUM_APP_ID`: Mantium app ID - you can find this from a deployed plugin
- `MANTIUM_BEARER_TOKEN`: Your Mantium Bearer Token
- `OPENAI_API_KEY`: Your OpenAI API key (if using OpenAI).
- `AZURE_OPENAI_API_KEY`: Your Azure OpenAI key (if using Azure OpenAI).
- `AZURE_OPENAI_ENGINE`: The name of the Azure OpenAI engine (e.g., "gpt-3.5-turbo").
- `AZURE_OPENAI_API_BASE`: Base URL for the Azure OpenAI API

## Sample .env file:

# app config
API_TYPE= # openai or azure

# OpenAI API Key  
OPENAI_API_KEY=sk-xxx
  
# Azure-specific settings  
AZURE_OPENAI_ENGINE=# name of the engine to use
AZURE_OPENAI_API_KEY=# API key for the Azure OpenAI  
AZURE_OPENAI_API_BASE=# base URL for the Azure OpenAI API
  
# Mantium-specific settings  
MANTIUM_APP_ID=# Mantium app ID - you can find this from a deployed plugin
MANTIUM_BEARER_TOKEN=# You can find this by making a request from the plugin screen with devtools open. Look at the payload.