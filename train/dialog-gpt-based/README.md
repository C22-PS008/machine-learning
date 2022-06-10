# Dialogue GPT Based

## Dependencies
Depedencies used is `transformer 4.19`, `tokenizer`, `datasets`, `sentencepiece`, `tqdm`, and `torch`.

## Dataset and Model
Datasets used is `blended_skill_talk` and `tokenize_indonlu_dataset`.
```
blended_skill_dataset = load_dataset("blended_skill_talk")

torch_train_dataset = DataLoader(tokenize_indonlu_dataset["train"],shuffle=True, collate_fn=pytorch_data_collator, batch_size=16)
torch_validation_dataset = DataLoader(tokenize_indonlu_dataset["validation"], collate_fn=pytorch_data_collator, batch_size=16)
```

Model and tokenizer used is `GPT2` from `transformer`.
```
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2Model.from_pretrained('gpt2')
```
Tokenizer from `indonlu` also used.
```

```

## Preprocessing and Tokenizing
Delete things that didn't needed such as punctuation marks, spaces and (english) abbreviations.
```
DEFINE FUNCTION process_token_list(token_list):
    SET token_list[0] TO token_list[0].capitalize()
    SET quote_count TO 0

    FOR i, token IN enumerate(token_list):
        IF space IN token:
            IF token[1:] IN end_marks or token[1:] IN abbreviations:
                SET token_list[i] TO token[1:]
            IF token[1:] EQUALS quotes[1]:
                IF i < len(token_list)-1:
                    IF token_list[i + 1] IN abbreviations or (token_list[i + 1][0] EQUALS space and token_list[i + 1][1:] IN abbreviations):
                        SET token_list[i] TO token[1:]

        IF token[0] EQUALS space and token[1:] IN quotes:
            IF quote_count % 2 EQUALS 1:
                SET token_list[i] TO token[1:]
                SET quote_count TO 0
            ELSE:
                IF i < len(token_list)-1 and token_list[i + 1][0] EQUALS space:
                    SET token_list[i + 1] TO token_list[i + 1][1:]
                quote_count += 1

        IF token IN end_marks or token[1:] IN end_marks:
            IF i<len(token_list)-1:
                IF token_list[i + 1][0] != space:
                    SET token_list[i + 1] TO space + token_list[i + 1].capitalize()
                ELSE:
                    SET token_list[i + 1] TO space + token_list[i + 1][1:].capitalize()

    SET new_token_list TO [token FOR token IN token_list IF token != space and len(token) > 0]

    IF new_token_list[-1] not IN end_marks:
        new_token_list.append(end_marks[0])      

    RETURN new_token_list
```

## Training and Save the Model
