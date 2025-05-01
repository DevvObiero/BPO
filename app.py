from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import logging

app = Flask(__name__)
CORS(app)

# Logging Configuration
logging.basicConfig(level=logging.DEBUG)

# Set your OpenAI API key here (your friend needs to replace this)
openai.api_key = 'your-openai-api-key-here'  # Replace with actual API key

# Dictionary of custom responses (all keys in lowercase)
custom_response = {
    "hi": "Hello There, how can I assist you?",
    "hello": "Hey! How can I help you today",
    "hey": "Hi, how can i be of assistance",
    "what is nftbpo": "We are a tech service company that offers a wide variety of services to businesses in Kenya",
    "how are you": "Im just code but, Im running great, anyway how can I help you?",
    "who made you": "A genius developer called Don J from the Eclipse team",
    "what is nftbpo about": "It is about helping and providing services in the tech space",
    "bye": "Come back soon I will be waiting",
    "what is your name": "My name is TraceyAI, Your helpful assistant",
    "tell me a joke": "Why dont scientists trust atoms? Because they make up everything!",
    "what is the weather today": "I am not sure, check your local weather service",
    "what do you do": "We are a tech service company that offers a wide variety of services to businesses in Kenya",
    "how can i reset my password": "You can reset your password by clicking on the 'Forgot Password' link on the login page. Follow instructions to reset your password.",
    "do you offer 24/7 support": "Yes we do. You can reach us anytime via our support email or chat.",
    "what services do you offer": "We offer a wide range of services including app development, AI integration, cloud solutions, IT consultancy, web development and mobile app development.",
    "how do i get a quote for a project": "You can get a quote by filling out the contact form on our website or by reaching out to us on email. We normally respond within 24 hours.",
    "can i get a demo of your services": "Yes we offer demos for our services. Please contact us to schedule a demo by filling out the contact form on the website.",
    "what is your response time": "Our response time is usually within 24 hours but if its urgent call the support line and we will assist you as soon as possible.",
    "do you refund": "Yes we do. If you are not satisfied with our services, please contact us within 30 days of purchase for a full refund.",
    "do you build e-commerce websites": "Yes we do. We have a team of experts who can help you build a fully functional e-commerce website.",
    "do you offer seo services": "Yes we do. We have a team of experts who can help you with SEO and digital marketing.",
    "is my data safe with you": "Yes we take data security very seriously. We use the latest encryption and security measures to protect your data.",
    "do you offer training": "Yes we do. We offer training for all our services. Please contact us for more information."
}

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json['message'].lower()  # Convert to lowercase
    except (KeyError, TypeError, AttributeError):
        logging.error("Invalid request: missing or malformed 'message' in JSON")
        return jsonify({'error': 'Invalid request: missing message'}), 400

    bot_reply = custom_response.get(user_message)

    if not bot_reply:
        try:
            # Fall back to OpenAI
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful chatbot assistant."},
                    {"role": "user", "content": user_message}
                ]
            )
            bot_reply = response['choices'][0]['message']['content']
            logging.debug(f"User message: {user_message}")
            logging.debug(f"Bot reply: {bot_reply}")
        except Exception as e:
            logging.error(f"OpenAI API error: {e}")
            bot_reply = "There seems to be an issue with the AI service. Please try again later."

    return jsonify({'reply': bot_reply})

if __name__ == '__main__':
    app.run(debug=True)