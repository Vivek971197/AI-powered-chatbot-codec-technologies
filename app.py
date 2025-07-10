from flask import Flask, request, jsonify, render_template
from transformers import pipeline

app = Flask(__name__)

# Load fast and smart model
chatbot = pipeline("text2text-generation", model="google/flan-t5-base")

# Generate chatbot response
def generate_reply(user_input):
    prompt = f"Answer politely and helpfully: {user_input}"
    result = chatbot(prompt, max_length=100, temperature=0.7)
    return result[0]['generated_text'].strip()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")
    response = generate_reply(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
