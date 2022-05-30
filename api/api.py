from typing_extensions import Required
from unittest import result
from click import argument
from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse

from matplotlib.pyplot import get
from transformers import RoFormerForQuestionAnswering

user_input_args=reqparse.RequestParser()
user_input_args.add_argument('message', type=str, help='message')
user_input_args.add_argument('age', type=int, help='age')


app=Flask(__name__)
api=Api(app)

def load_ner_model(input):
    from transformers import pipeline
    model_checkpoint = "chanifrusydi/bert-finetuned-ner"
    token_classifier = pipeline("token-classification", model=model_checkpoint, aggregation_strategy="simple")
    result=token_classifier(input)
    if len(result)!=0:
        return result
    else:
        return "No entity found"

user_input_dict={}

class get_user_call_name(Resource):
    def post(self):
        user_input=user_input_args.parse_args()
        user_message=user_input["message"]
        result=model(user_message)
        # for i in range(len(result)):
        #     if result[0].get('entity_group')=='PER':
        #         words=result[0].get('word')
        #         print(words)
        #         return {"result":words}
        # else:
        #     return {"result":"No entity found"}
        if result!="No entity found":
            for i in range(len(result)):
                if result[i].get('entity_group')=='PER':
                    words=result[i].get('word')
                    greet_user="Hello, " + words + "!"
                    return {'greet_user':greet_user}
        else:
            return {'greet_user':"Hello, I cant get your name, would you mind to type it again?."}

class get_age(Resource):
    def post(self):
        user_input=user_input_args.parse_args()
        user_age=user_input["age"]
        user_input_dict['age']=user_age
        return jsonify(user_input_dict)


api.add_resource(get_user_call_name, '/chatbot/getusercallname')
api.add_resource(get_age, '/chatbot/getage')

app.run(host="localhost",port=5000,debug=True)