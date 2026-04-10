from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder='static')


def get_response(user_input):
    user_input = user_input.lower()

    if 'exit' in user_input or 'quit' in user_input or 'goodbye' in user_input:
        return "Goodbye! Have a great day! We hope that we served you well."
    
    if 'hello' in user_input or 'hi' in user_input:
        return "Hello! How can I assist you today? Please describe your symptoms or ask any health-related questions."

    elif 'how are you' in user_input:
        return "I'm just a chatbot, but I'm here to help you!"

    elif 'thank you' in user_input:
        return "You're welcome! 😊"

    elif 'what is your name' in user_input:
        return "I'm your hospitality chatbot."

    elif 'shortness of breath' in user_input or 'chest pain' in user_input:
        return "⚠️ Serious symptoms! Please seek immediate medical attention."

    elif 'dizziness' in user_input and 'shortness of breath' in user_input:
        return "⚠️ This may be serious. Seek medical help immediately."

    elif 'fever' in user_input and 'cough' in user_input:
        return "You may have infection. Take rest, fluids, and consult doctor if needed."

    elif 'fever' in user_input or 'headache' in user_input:
        return "You may have fever or headache. Take Paracetamol and rest."

    elif 'fatigue' in user_input or 'muscle pain' in user_input:
        return "You may have fatigue or muscle pain. Rest and stay hydrated."

    elif 'body aches' in user_input or 'chills' in user_input:
        return "You may have body aches or chills. Rest and take fluids."

    elif 'loss of taste' in user_input or 'loss of smell' in user_input:
        return "Loss of taste/smell detected. Monitor symptoms and consult doctor."

    elif 'stomach' in user_input or 'abdominal pain' in user_input:
        return "You may have stomach issues. Eat light food and stay hydrated."

    elif 'diarrhea' in user_input or 'vomiting' in user_input:
        return "Drink ORS and stay hydrated."

    elif 'cough' in user_input or 'sore throat' in user_input:
        return "You may have cough or sore throat. Try warm fluids."

    elif 'congestion' in user_input or 'runny nose' in user_input:
        return "Steam inhalation can help with congestion."

    elif 'rash' in user_input or 'itching' in user_input:
        return "Apply anti-itch cream and avoid scratching."

    elif 'nausea' in user_input or 'dizziness' in user_input:
        return "Take rest and drink fluids."

    else:
        return "I'm sorry, I didn't understand that. Please describe your symptoms clearly."


@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get('message', '')

    response = get_response(user_input)

    return jsonify({'response': response})


if __name__ == '__main__':
    app.run(debug=True)