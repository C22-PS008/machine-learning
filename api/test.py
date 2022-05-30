from lib2to3.pgen2.tokenize import tokenize
from statistics import mode
import json_parser
import json

import tokenizers


def model(input):
    from transformers import pipeline
    model_checkpoint = "chanifrusydi/bert-finetuned-ner"
    token_classifier = pipeline("token-classification", model=model_checkpoint, aggregation_strategy="simple")
    result=token_classifier(input)
    entity_group=result[0].get('entity_group')
    word=result[0].get('word')
    print(result[0].get('entity_group'))

    return entity_group,word

# token_classification=model("My name is Joko and I work at Universitas Indonesia in Jakarta.")
# print(token_classification)
x =  '{ "name":"John", "age":30, "city":"New York"}'
user_input=json_parser.parse(x).get("name")
print(user_input)
def model(input):
    from transformers import TFBertForTokenClassification, pipeline, AutoTokenizer
    model_checkpoint = "chanifrusydi/bert-finetuned-ner"
    token_classifier = pipeline("token-classification", model=model_checkpoint,  aggregation_strategy="simple")
    result=token_classifier(input)
    # entity_group=[]
    # word=[]
    if len(result)>=0:
        return result
    else:
        return "No entity found"
        
hasil=model("My name is")

print(len(hasil))
print(hasil)
for i in range(len(hasil)):
    if hasil[i].get('entity_group')=='PER':
        words=hasil[i].get('word')
        print(words)