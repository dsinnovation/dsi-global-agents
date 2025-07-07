# DSI.Global | Bank Support Bot (MVP)
# Built with Twilio + OpenAI

from twilio.rest import Client
import openai

# Placeholder config
ACCOUNT_SID = "your_sid"
AUTH_TOKEN = "your_token"
OPENAI_KEY = "your_openai_key"

client = Client(ACCOUNT_SID, AUTH_TOKEN)
openai.api_key = OPENAI_KEY

def generate_response(message):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": message}]
    )
    return response['choices'][0]['message']['content']

# Simulate message
print(generate_response("How do I check my account balance?"))
