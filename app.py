from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')

    url = f"https://api.duckduckgo.com/?q={query}&format=json"
    response = requests.get(url).json()

    results = []
    if "RelatedTopics" in response:
        for item in response["RelatedTopics"][:5]:
            if "Text" in item:
                results.append(item["Text"])

    return jsonify(results)

if __name__ == '__main__':
    app.run(port=5000)