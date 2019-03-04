import os
import random

import numpy as np

import keras
from keras_wc_embd import get_batch_input, get_embedding_weights_from_file

from utils.yaml import read_yaml
from utils.embed import get_dicts_generator, get_char_hidden_layer

###############################################################################
# READ-IN DATA

# Measure
read_in_measures = read_yaml("../dataset/measure/measure.yaml")
measure = read_in_measures[161]['dual retail']['RC'].split(' ')
print(measure)
print(len(measure))

# Provision
read_in_provisions = read_yaml("../dataset/provision/gatt.yaml")
provision = read_in_provisions['III'][4].split(' ')
print(provision)
print(len(provision))

# Legality
read_in_legality = read_yaml("../dataset/label/legality.yaml")
print(read_in_legality[161]['Dual Retail']['GATT III:4'])

# Aggregate all texts data from measure and provision
sentences = [
    measure,
    provision
]

measures = [
    measure
]

provisions = [
    provision
]

###############################################################################
# Generate Lookup Table
print('Get dictionaries....')
dict_generator = get_dicts_generator(
    word_min_freq=1,
    char_min_freq=1,
    word_ignore_case=False,
    char_ignore_case=False,
)

for sentence in sentences:
    print(sentence)
    dict_generator(sentence)

word_dict, char_dict, max_word_len = dict_generator(return_dict=True)
print(len(word_dict))
print(len(char_dict))
print(max_word_len)
###############################################################################
# Define Input
word_input_measure = keras.layers.Input(shape=(None,),
                                        name='Input_Word_Measure')
word_input_provision = keras.layers.Input(shape=(None,),
                                          name='Input_Word_Provision')
char_input_measure = keras.layers.Input(shape=(None, max_word_len),
                                        name='Input_Char_Measure')
char_input_provision = keras.layers.Input(shape=(None, max_word_len),
                                          name='Input_Char_Provision')
###############################################################################
# Define  Word Embedding Layer
word_embd_weights = get_embedding_weights_from_file(
    word_dict,
    'GloVec/glove.6B.100d.txt',
    ignore_case=False)  # load GloVec pre-weights

word_embd_dim = 100

word_embd_weights = [word_embd_weights]
word_embd_trainable = True
word_mask_zero = True

word_embd_layer = keras.layers.Embedding(
    input_dim=len(word_dict),
    output_dim=word_embd_dim,
    mask_zero=word_mask_zero,
    weights=word_embd_weights,
    trainable=word_embd_trainable,
    name='Embedding_Word')

word_embd_measure = word_embd_layer(word_input_measure)
word_embd_provision = word_embd_layer(word_input_provision)

# Define Char Embedding Layer

char_embd_dim = 50

char_embd_trainable = True
char_mask_zero = True
char_embd_weights = None

char_embd_pre_layer = keras.layers.Embedding(
    input_dim=len(char_dict),
    output_dim=char_embd_dim,
    mask_zero=char_mask_zero,
    weights=char_embd_weights,
    trainable=char_embd_trainable,
    name='Embedding_Char_Pre')

char_hidden_layer = get_char_hidden_layer(
    char_dict_len=len(char_dict),
    max_word_len=max_word_len,
    char_hidden_dim=150,
    char_hidden_layer_type='lstm')

for i, layer in enumerate(char_hidden_layer):
    print("i", i)
    if i == len(char_hidden_layer) - 1:
        name = 'Embedding_Char'
    else:
        name = 'Embedding_Char_Pre_%d' % (i + 1)
    print(name)
    char_embd_layer = keras.layers.TimeDistributed(layer=layer, name=name)

char_embd_measure = char_embd_layer(char_embd_pre_layer(char_input_measure))
char_embd_provision = char_embd_layer(char_embd_pre_layer(char_input_provision))

###############################################################################

# Encode
word_char_embd_measure = keras.layers.Concatenate(
    name='WordCharEmbeddingMeasure')(
    [word_embd_measure, char_embd_measure])

word_char_embd_provision = keras.layers.Concatenate(
    name='WordCharEmbeddingProvision')(
    [word_embd_provision, char_embd_provision])

# ###############################################################################
# Prediction Model
print('Create model...')

# Concatenate [MeasureEmbd, ProvisionEmbd]
concat_embd = keras.layers.concatenate([word_char_embd_measure,
                                        word_char_embd_provision], axis=0)

lstm_layer = keras.layers.Bidirectional(
    keras.layers.LSTM(units=50),
    name='Bi-LSTM')(concat_embd)

dense_layer = keras.layers.Dense(
    units=2,
    activation='softmax',
    name='Dense')(lstm_layer)

model = keras.models.Model(inputs=[word_input_measure,
                                   char_input_measure,
                                   word_input_provision,
                                   char_input_provision],
                           outputs=dense_layer)

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy'])

model.summary()  # print model spec

###############################################################################
# Forward Path

measure_input = get_batch_input(measures,
                                max_word_len=max_word_len,
                                word_dict=word_dict,
                                char_dict=char_dict)
print(measure_input[0].shape)
print(measure_input[1].shape)


provision_input = get_batch_input(provisions,
                                  max_word_len=max_word_len,
                                  word_dict=word_dict,
                                  char_dict=char_dict)
print(provision_input[0].shape)
print(provision_input[1].shape)

y = keras.utils.to_categorical([1], num_classes=2)

model.fit([measure_input[0],
           measure_input[1],
           provision_input[0],
           provision_input[1]],
          y)
###############################################################################

# print(keras.utils.to_categorical(1))  # if 1, it's consistent
if __name__ == "__main__":
    pass
