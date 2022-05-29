import requests
import json

url='http://localhost:8000/chatbot'
endpoint='simulation'
api_endpoint=url+'/'+endpoint
print(api_endpoint)

def start_chat():
    print("Hello, im chatbot, I will help you find suitables categories for you. Okay, how should I call you?")
    user_input=input()
    response=requests.post(api_endpoint,data={"message":user_input})
    return response.json()

bot=start_chat()
print(bot)
