import os  
from dotenv import load_dotenv  
from azure_gpt import create_azure_chat_completion  
from openai_gpt import create_openai_chat_completion  
from mantium_data import fetch_mantium_data
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity 
  
load_dotenv()

def score_mantium_responses(mantium_data):
    scored_responses = [(result['text'], result['score']) for result in mantium_data['results'][0]['results']]
    best_response = max(scored_responses, key=lambda x: x[1])
    return best_response[0]

def combined_scores(user_input, mantium_responses, mantium_scores):
    # Calculate the similarity scores
    vectorizer = TfidfVectorizer()
    all_text = [user_input] + mantium_responses
    tfidf_matrix = vectorizer.fit_transform(all_text)
    similarity_scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])[0]
    
    # Combine the Mantium scores and similarity scores
    combined_scores_dict = {}
    for i, (mantium_score, similarity_score) in enumerate(zip(mantium_scores, similarity_scores)):
        combined_scores_dict[i] = mantium_score * similarity_score

    # Find the index of the highest combined score
    best_response_index = max(combined_scores_dict, key=combined_scores_dict.get)
    return best_response_index


  
def generate_response(query, api_type, mantium_data):
    conversation = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": query},
    ]

    engine = os.getenv("AZURE_OPENAI_ENGINE") if api_type == "azure" else "gpt-3.5-turbo"
    
    mantium_responses = mantium_data
    mantium_scores = [1 for _ in range(len(mantium_responses))]  # Assuming equal weight for all responses for now
    best_response_index = combined_scores(query, mantium_responses, mantium_scores)
    
    best_mantium_response = mantium_data[best_response_index]
    conversation.append({"role": "assistant", "content": best_mantium_response})

    if api_type == "azure":
        response = create_azure_chat_completion(engine, conversation)
    else:
        response = create_openai_chat_completion(engine, conversation)

    return response['choices'][0]['message']['content'], best_mantium_response


if __name__ == "__main__":  
    api_type = os.getenv("API_TYPE", "openai")  
    mantium_app_id = os.getenv("MANTIUM_APP_ID")  
    mantium_bearer_token = os.getenv("MANTIUM_BEARER_TOKEN")  
  
    while True:
        user_input = input("Please enter your question: ")

        mantium_results = fetch_mantium_data(mantium_app_id, mantium_bearer_token, user_input)
        if mantium_results:
            if 'results' in mantium_results and len(mantium_results['results']) > 0:
                mantium_answers = [result['text'] for result in mantium_results['results'][0]['results']]

                final_response, best_mantium_response = generate_response(user_input, api_type, mantium_answers)
                print("\nBest Mantium response:", best_mantium_response)
                print("Final response:", final_response, "\n")
            else:
                print("There was an error fetching data from Mantium. The 'results' key is missing or empty.")
        else:
            print("There was an error fetching data from Mantium.")
