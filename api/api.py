from signal import SIGKILL
from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse
import pathlib

from tensorboard import summary
user_input_args=reqparse.RequestParser()
user_input_args.add_argument('message', type=str, help='message')
user_input_args.add_argument('age', type=int, help='age')
import to_pdf


app=Flask(__name__)
api=Api(app)

def check_if_model_downloaded(model_name):
    import os
    model_path=os.path.join("../model/", model_name)
    relative_path=pathlib.Path(model_path)
    if relative_path.exists():
        return relative_path
    else:
        return False
def load_ner_model(input):
    from transformers import pipeline
    model_checkpoint = "chanifrusydi/bert-finetuned-ner"
    token_classifier = pipeline("token-classification", model=model_checkpoint, aggregation_strategy="simple")
    result=token_classifier(input)
    if len(result)!=0:
        return result
    else:
        return "No entity found"

def load_chatbot_model(input):
    from transformers import pipeline
    model_checkpoint = "chanifrusydi/bert-finetuned-chatbot"
    chatbot_model = pipeline("question-answering", model=model_checkpoint)
    result=chatbot_model(input)
    if len(result)!=0:
        return result
    else:
        return "No entity found"

user_input_dict={}

class get_user_call_name(Resource):
    def post(self):
        user_input=user_input_args.parse_args()
        user_message=user_input["message"]
        result=load_ner_model(user_message)
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

class create_pdf(Resource):
    def post(self):
        input=user_input_args.parse_args()
        name=input["name"]
        skill=input["skill"]
        profession=input["profession"]
        summary=input["summary"]
        json_dict={'name':name, 'skill':skill, 'profession':profession, 'summary':summary}
        with open('../../export_pdf/user.json', 'w') as json_file:
            json.dump(personDict, json_file)
        to_pdf.create_pdf('user.json','user.pdf')
        return jsonify(json_dict)
        
@app.route('/uploads/export_pdf/user.pdf')
def download_file(filename):
    return send_from_directory(directory='../../export_pdf',filename='user.pdf' , as_attachment=True)

api.add_resource(get_user_call_name, '/chatbot/getusercallname')
api.add_resource(get_age, '/chatbot/getage')
api.add_resource(create_pdf, '/chatbot/createpdf')

app.run(host="0.0.0.0",port=23450,debug=True)