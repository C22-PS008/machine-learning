from unittest import result


def model(input):
    from transformers import pipeline
    model_checkpoint = "chanifrusydi/bert-finetuned-ner"
    token_classifier = pipeline("token-classification", model=model_checkpoint, aggregation_strategy="simple")
    result=token_classifier(input)
    entity_group=result[0].get('entity_group')
    word=result[0].get('word')
    print(result[0].get('entity_group'))

    return entity_group,word

token_classification=model("My name is Joko and I work at Universitas Indonesia in Jakarta.")
print(token_classification)