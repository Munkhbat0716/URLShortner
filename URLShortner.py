from flask import Flask, request, jsonify, redirect
import string
import random

app = Flask(__name__)

# In-memory storage for shortened URLs
url_map = {}

# Function to generate a short URL
def generate_short_url():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.json.get('url')
    if not original_url:
        return jsonify({"error": "Missing URL"}), 400

    short_url = generate_short_url()
    url_map[short_url] = original_url

    return jsonify({"short_url": f"http://localhost:5000/{short_url}"})

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
    original_url = url_map.get(short_url)
    if original_url:
        return redirect(original_url)
    return jsonify({"error": "URL not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
