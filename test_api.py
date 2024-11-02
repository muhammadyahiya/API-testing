from flask import Flask, request, jsonify
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Access Hugging Face API URL and Token from environment variables
HUGGING_FACE_API_URL = os.getenv("HUGGING_FACE_API_URL")
API_TOKEN = os.getenv("HUGGING_FACE_API_TOKEN")

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

@app.route('/predict', methods=['GET'])
def get_prediction():
    # Send a GET request to the Hugging Face API
    response = requests.get(HUGGING_FACE_API_URL, headers=headers)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": response.text}), response.status_code

@app.route('/predict', methods=['POST'])
def post_prediction():
    # Get JSON data from the POST request
    data = request.get_json()
    
    # Send a POST request to the Hugging Face API
    response = requests.post(HUGGING_FACE_API_URL, headers=headers, json=data)
    
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": response.text}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
