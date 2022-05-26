from lib2to3.pgen2 import token
from fastapi import FastAPI

app = FastAPI()


def model(input):
    from transformers import pipeline
    model_checkpoint = "chanifrusydi/bert-finetuned-ner"
    token_classifier = pipeline("token-classification", model=model_checkpoint, aggregation_strategy="simple")
    result=token_classifier(input)
    return result

@app.get("/")
async def root():
    token_classification=model("Nama saya Joko, saya suka coding Python")
    return{'token':token_classification}
    
