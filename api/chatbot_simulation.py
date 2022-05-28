import requests
import json

def start_chat():
    print("Hello, im chatbot, I will help you find suitables categories for you. Okay, how should I call you?")
    user_input=input()
    response=requests.post("http://localhost:8000/api/chatbot_simulation",json={"message":user_input})
    return response.json()

bot=start_chat()
responses=json.loads(bot)
