import os
import requests
from dotenv import load_dotenv

load_dotenv()

def fetch_mantium_data(app_id, bearer_token, query):
    try:
        url = f'https://{app_id}.apps.mantiumai.com/chatgpt/query'
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': f'Bearer {bearer_token}',
            'content-type': 'application/json',
            'user-agent': 'Mantium API Client/v.0.1.0',
        }
        data = {"queries": [query]}
        response = requests.post(url, headers=headers, json=data)

        if response.status_code != 200:
            response.raise_for_status()

        response_data = response.json()

        print("\nMantium responses:")
        for i, result in enumerate(response_data['results'][0]['results']):
            print(f"{i + 1}. {result['text']} (score: {result['score']})")

        return response_data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching data: {e}")
        return None
