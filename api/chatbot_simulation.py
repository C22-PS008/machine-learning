import requests

url='http://127.0.0.1:5000/chatbot'
endpoint='getusercallname'
api_endpoint=url+'/'+endpoint
print(api_endpoint)

print("Hello, im chatbot, I will help you find suitables categories for you. Okay, how should I call you?")
user_input=input()
print(type(user_input))
post_json={'message':user_input}
response=requests.post(endpoint,json=post_json)
print(response.json())

print("Okay, what is your age?")
user_input=input()
endpoint='get_age'
api_endpoint=url+'/'+endpoint
age_response=requests.post(api_endpoint,json={'age':user_input})
print(age_response.json())

