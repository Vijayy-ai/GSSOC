import requests
from flask import Flask, request, jsonify, render_template,url_for
import api_config

app = Flask(__name__)


api_key = api_config.get_openai_api_key()

# Replace 'your_openai_api_key' with your actual OpenAI API key
openai_api_key = 'your_openai_api_key'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    prompt = data.get('prompt')

    openai_url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer " + api_config.get_openai_api_key()
    }
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content":"This assistant is specialized in Ayurveda, so only focus on ayurveda and health don't give answer of other field questions. It can answer questions about Ayurvedic herbs, treatments, principles, health, Disease, health issue, trees, medicines."},
            {"role": "user", "content": prompt}
            
        ]
    }

    response = requests.post(openai_url, headers=headers, json=payload)

    if response.status_code == 200:
        message = response.json()['choices'][0]['message']['content'].strip()
        return jsonify(message=message)
    else:
        return jsonify(message="Error occurred while fetching the response.")

if __name__ == '__main__':
    app.run(debug=True)
























# import requests
# from flask import Flask, request, jsonify, render_template,url_for
# import api_config

# app = Flask(__name__)

# # Replace 'your_openai_api_key' with your actual OpenAI API key
# openai_api_key = api_config.get_openai_api_key()

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/ask', methods=['POST'])
# def ask():
#     data = request.get_json()
#     health_issue = data.get('health_issue')

#     openai_url = "https://api.openai.com/v1/chat/completions"
#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {openai_api_key}"
#     }
#     payload = {
#         "model": "gpt-3.5-turbo",
#         "messages": [
#             {"role": "system", "content": "You are a knowledgeable Ayurveda assistant focused on providing information about health, wellness, and Ayurvedic medicine."},
#             {"role": "user", "content": health_issue}
#         ]
#     }

#     response = requests.post(openai_url, headers=headers, json=payload)

#     if response.status_code == 200:
#         message = response.json()['choices'][0]['message']['content'].strip()
#         return jsonify(message=message)
#     else:
#         return jsonify(message="Error occurred while fetching the response.")

# if __name__ == '__main__':
#     app.run(debug=True)








# import requests
# from flask import Flask, request, jsonify, render_template, url_for
# import api_config

# app = Flask(__name__)

# api_key = api_config.get_openai_api_key()

# # Function to check if the prompt is related to health, Ayurveda, and Ayurvedic medicines
# def is_ayurvedic_related(prompt):
#     """
#   Checks if the prompt is related to health, Ayurveda, and Ayurvedic medicines.
#   This function now also includes a check using the GPT-3 to classify whether the
#   prompt is related to Ayurveda, which can account for a wider range of health topics.
#   """
#     # Add more relevant keywords here
#     health_related_keywords = ['ayurveda', 'ayurvedic', 'health', 'wellness', 'medicine', 'herbs', 'tree','stomach', 'pain', 'disease', 'treatment', 'therapy']

#     # Check if the prompt contains any of the keywords
#     for keyword in health_related_keywords:
#         if keyword in prompt.lower():
#             return True

#     # Use the GPT-3 API to classify the prompt as related to Ayurveda or not
#     openai_url = "https://api.openai.com/v1/classifications"
#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer " + api_config.get_openai_api_key()
#     }
#     payload = {
#         "model": "text-classification-0001",
#         "prompt": prompt,
#         "labels": ["ayurveda", "not_ayurveda"]
#     }

#     response = requests.post(openai_url, headers=headers, json=payload)

#     if response.status_code == 200:
#         label = response.json()['choices'][0]['label']
#         return label == "ayurveda"
#     else:
#         return False

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/ask', methods=['POST'])
# def ask():
#     data = request.get_json()
#     prompt = data.get('prompt')

#     # Check if the prompt is related to health, Ayurveda, and Ayurvedic medicines
#     if not is_ayurvedic_related(prompt):
#         return jsonify(message="Sorry, your question does not seem to be related to Ayurveda. " \
#                                 "If you believe this is an error, please rephrase your question or provide more context.")

#     openai_url = "https://api.openai.com/v1/chat/completions"
#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer " + api_config.get_openai_api_key()
#     }
#     payload = {
#         "model": "gpt-3.5-turbo",
#         "messages": [
#             {"role": "system", "content": """
# Checks if the prompt is related to health, Ayurveda, and Ayurvedic medicines.
# This function now also includes a check using the GPT-3 to classify whether the
# prompt is related to Ayurveda, which can account for a wider range of health topics.
# """},
#             {"role": "user", "content": prompt}
#         ]
#     }

#     response = requests.post(openai_url, headers=headers, json=payload)

#     if response.status_code == 200:
#         message = response.json()['choices'][0]['message']['content'].strip()
#         return jsonify(message=message)
#     else:
#         return jsonify(message="Error occurred while fetching the response.")

# if __name__ == '__main__':
#     app.run(debug=True) 