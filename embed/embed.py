import keras
from keras_wc_embd import get_dicts_generator, get_embedding_layer, \
    get_batch_input, get_embedding_weights_from_file

from utils.yaml import read_yaml

# Example Sentences in Gov Measure
measures = read_yaml("../dataset/measure/measure.yaml")
sentence1 = measures[161]['dual retail']['RC'].split(' ')
sentence2 = measures[161]['dual retail']['REP'].split(' ')

sentences = [
    sentence1,
    sentence2,
]


# Generate Lookup Table
dict_generator = get_dicts_generator(
    word_min_freq=1,
    char_min_freq=1,
    word_ignore_case=False,
    char_ignore_case=False,
)
for sentence in sentences:
    dict_generator(sentence)

word_dict, char_dict, max_word_len = dict_generator(return_dict=True)

word_embd_weights = get_embedding_weights_from_file(
    word_dict,
    'pretrained/glove.6B.300d.txt',
    ignore_case=False)

# Define Embedding Model (Word-Character Model)
inputs, embd_layer = get_embedding_layer(
    word_dict_len=len(word_dict),
    char_dict_len=len(char_dict),
    max_word_len=max_word_len,
    word_embd_dim=300,
    char_embd_dim=50,
    char_hidden_dim=150,
    word_embd_weights=word_embd_weights,
    char_hidden_layer_type='lstm')  # lstm, 'lstm', 'gru', 'cnn'

model = keras.models.Model(inputs=inputs, outputs=embd_layer)
model.summary()

# One hot Encoding
word_embd_input, char_embd_input = get_batch_input(
    sentences,
    max_word_len=max_word_len,
    word_dict=word_dict,
    char_dict=char_dict,
)
print(sentences)
print("word_embed_input:", word_embd_input, word_embd_input.shape)
print("char_embed_input:", char_embd_input, char_embd_input.shape)

#  Load pre-trained embeddings for initializing the weights


if __name__ == "__main__":
    print(measures)
    print(sentence1)
    print(sentence2)
    print(word_dict)
    print(char_dict)
    print("char_dict len: ", len(char_dict))
    print(max_word_len)
    print("max sentence len: ", max(len(sentence1), len(sentence2)))
