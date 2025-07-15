from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load a conversational pipeline
chatbot = pipeline("conversational", model="facebook/blenderbot-400M-distill")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"response": "Please send a message."})
    response = chatbot(user_message)[0]['generated_text']
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
