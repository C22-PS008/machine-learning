# machine-learning

## This repository is the repository of machine learning cohort for Bangkit Capstone.

Huge thanks to [HuggingFace](https://huggingface.co) for easy to use pipeline, dataset,base model.

## Code Reference, Base Model, Dataset

-[Chatbot Intent Based](/train/chatbot-intents-based/README.md)
-[Named Entity Recognition](/train/named-entity-recognition/README.md)
-[Dialogue GPT Based](/train/dialog-gpt-based/README.md)
-[Dialogue Summarization](/train/dialogue-summarization/README.md)

## How to use the api:

### Make sure you have the following environment set:

  Python 3.6+, PyTorch 1.1.0+, TensorFlow 2.0+.
  make sure your environment variable for 'python' is python3 and not python2  (you can check by typing `python --version`)

1. First Method :

```bash
    sh api.sh
```

  This will depedencies and run api code on api directory.
2. Second Method

```
  pip install -r requirement.txt
  python api.py 
```
