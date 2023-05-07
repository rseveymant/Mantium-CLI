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

- `MANTIUM_API_KEY`: Your Mantium API key.
- `OPENAI_API_KEY`: Your OpenAI API key (if using OpenAI).
- `AZURE_OPENAI_KEY`: Your Azure OpenAI key (if using Azure OpenAI).
- `AZURE_OPENAI_ENGINE`: The name of the Azure OpenAI engine (e.g., "gpt-3.5-turbo").
