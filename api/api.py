from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import chatbot_simulation

app=Flask(__name__)
api=Api(app)

def model(input):
    from transformers import pipeline
    model_checkpoint = "chanifrusydi/bert-finetuned-ner"
    token_classifier = pipeline("token-classification", model=model_checkpoint, aggregation_strategy="simple")
    result=token_classifier(input)
    entity_group=[]
    word=[]
    if len(result)>=0:
        for i in range(len(result)):
            entity_group_individual=result[i].get('entity_group')
            entity_group.append(entity_group_individual)
            word_individual=result[i].get('word')
            word.append(word_individual)
        return entity_group,word
    else:
        return "No entity found"
class Chatbot(Resource):
    def post(self):
        user_input=request.json['message']
        bot=chatbot_simulation(user_input)
        return bot
    def get(self):
        return "Hello, im chatbot, I will help you find suitables categories for you. Okay, how should I call you?"

api.add_resource(Chatbot, '/chatbot')


async def chatbot_simulation(input: str):
    user_input=input
    entity_group,word=model(user_input)
    if len(entity_group)>=0:
        for i in len(entity_group):
            if entity_group=="PER":
                return{"name":word[i]}
    else:
        return{"name":"No entity found"}
    

async def root():
    token_class=[]
    token_classification=model("My name is Joko and I work at Universitas Indonesia in Jakarta.")
    token_class.append(token_classification)
    return{'token':token_class}
    
app.run(host="localhost",port=5000)