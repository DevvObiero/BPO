from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import logging

app = Flask(__name__)
CORS(app)

#logging Configuration
logging.basicConfig(level=logging.DEBUG)


#Dictionary of custom responses
custom_response = {
    "hi": "Hello There, how can I assist you?",
    "hello": "Hey! How can I help you today",
    "hey": "Hi, how can i be of assistance",
    "what is NFTBPO": "We are a tech service company that offers a wide variety of services to bussines in kenya",
    "how are you": "Im just code but, Im running great, anyway how can I help you?",
    "who made you": "A genius developer called Don J from the Eclipse team",
    "what is NFTBPO about": "It is about helping and providing services in the tech space",
    "bye": "Come back soon I will be waiting",
    "What your name": "My name is TraceyAI, Your helpful assistant",
    "Tell me a joke": "why dont scientists trust atoms? Because they make up everything!",
    "what is the weather today": "I am not sure, check your local weather service",
    "what do you do": "We are a tech service company that offers a wide variety of services to businesses in Kenya",
    "How can I reset my password": "You can reset your password by clicking on the 'Forgot Password' link on the login page. Follow instructions to reset your password.",
    "Do you offer 24/7 suport": "Yes we do.You can reach us anytime via our support email or chat.",
    "what services do you offer": "We offer a wide range of services including app development, AI intergration, cloud solutions, IT consultancy, web development and mobile app development.",
    "How do I get a quote for a project": "You can get a quote by filling out the contact form on our website or by reaching out to us on email. We normally respond within 24 hours.",
    "Can I get a demo of your services": "Yes we offer demos for our services. Please contact us to schedule a demo by filling out the contact form on the website.",
    "What is your response time": "Our response time is ussually within 24 hours but if its urgent call the support line and we will assist you as soon as possible.",
    "Do you reffund": "yes we do. If you are not satisfied with our services, please contact us within 30 days of purchase for a full refund.",
    "Do you build e-commerce websites": "Yes we do. We have a team of experts who can help you build a fully functional e-commerce website.",
    "Do you offer SEO services": "Yes we do. We have a team of experts who can help you with SEO and digital marketing.",
    "Is my data safe with you": "Yes we take data security very seriously. We use the latest encryption and security measures to protect your data.",
    "Do you offer training": "Yes we do. We offer training for all our services. Please contact us for morer information.",

}
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    bot_reply = custom_response.get(user_message)

    if not bot_reply:
        try:
            # fall back to OpenAI      
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