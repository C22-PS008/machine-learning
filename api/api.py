from lib2to3.pgen2 import token
from fastapi import FastAPI

app = FastAPI()


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

@app.post("/api/chatbot_simulation")
async def root(message: user_input):
    entity_group,word=model(user_input)
    if entity_group=="PER":
        return{"name":word}
    else:
        return{"name":"No entity found"}
    

@app.get("/")
async def root():
    token_class=[]
    token_classification=model("My name is Joko and I work at Universitas Indonesia in Jakarta.")
    token_class.append(token_classification)
    return{'token':token_class}
    
