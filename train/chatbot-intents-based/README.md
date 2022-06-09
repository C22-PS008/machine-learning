# Intents Based Model
## Dependencies

Dependencies that used `Tensorflow`, `numpy`, `pandas`, `json` and `matplotllib`.

## Load data and Preprocessing
Load the dataset

```
with open('intents.json') as f:
    data = json.load(f)
```

Add the tag for each phrase
```
for intent in data['intents']:
  responses[intent['tag']] = intent['response']
  for lines in intent['input']:
    inputs.append(lines)
    tags.append(intent['tag'])
```

Delete punctuation from the phrase
```
data['inputs'] = data['inputs'].apply(lambda wrd:[ltrs.lower() for ltrs in wrd if ltrs not in string.punctuation])
data['inputs'] = data['inputs'].apply(lambda wrd: ''.join(wrd))
```

Preview of the data
| inputs      | tags |
| ----------- | ----------- |
| kisaran salary       | Penghasilan       |
| menjadi job   | Pekerjaan        |
| name  | Nama        |
| berkisar salary   | Penghasilan        |
| aku berusia age tahun   | Umur        |

## Train & Save the Model
The training process using Sequential model layers, using `bidirectional`, `LSTM`, `Dense` layers. Compiled with the `categorical_cross_entropy` loss function and `adam` optimizer. 
```
model = tf.keras.Sequential([
    tf.keras.layers.InputLayer(input_shape=(input_shape,)),
    tf.keras.layers.Embedding(vocabulary+1,10),
    tf.keras.layers.Bidirectional(LSTM(200,return_sequences=True)),
    tf.keras.layers.Bidirectional(LSTM(100,return_sequences=True)),
    tf.keras.layers.Bidirectional(LSTM(50,return_sequences=True)),
    tf.keras.layers.LSTM(25),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(output_length,activation="softmax")
])
```
Save the model as `chatbot_model.h5`
```
model.save('../../model/chatbot_model.h5')
```
