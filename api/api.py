from unittest import result
from click import argument
from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse



import json_parser

user_input_args=reqparse.RequestParser()
user_input_args.add_argument('message', type=str, required=True, help='message')


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
user_input_dict={}

class Chatbot(Resource):
    def post(self):
        user_input=user_input_args.parse_args()
        message=user_input["message"]
        result=model(message)
        return {'message':message}
        # try:
        #     for i in len(result):
        #         if entity_group[i]=='PER':
        #             greet_user="Hello, "+word[i]
        #             return {'result':result}
        # except(Exception):
        #     return Exception
    def get(self):
        pass

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
    
app.run(host="localhost",port=5000,debug=True)