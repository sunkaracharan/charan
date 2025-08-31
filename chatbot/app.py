from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import time
import webbrowser
from chatbot import Chat

app = Flask(__name__)
CORS(app)  # Enable CORS for API communication

@app.route('/')
def serve_index():
    return render_template('index.html')  # Serve index.html from templates folder

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        ch=Chat()
        data = request.get_json()
        print(data)
        prompt = data.get('prompt', '')
        if not prompt:
            return jsonify({'error': 'No prompt provided'}), 400
        try:
            response = ch.bot(prompt)
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        print(response)
        time.sleep(1)  # Simulate processing delay
        return jsonify({'response': response}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    webbrowser.open('http://localhost:5000')  # Automatically open browser
    app.run(debug=True, host='0.0.0.0', port=5000)