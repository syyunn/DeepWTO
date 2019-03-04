import os
import random

import numpy as np

import keras
from keras_wc_embd import get_embedding_layer, \
    get_batch_input, get_embedding_weights_from_file

from utils.yaml import read_yaml
from utils.embed import get_dicts_generator

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
# Create Embedding Layer (var inputs is a tensor holder)
#
# word_embd_weights = get_embedding_weights_from_file(
#     word_dict,
#     'GloVec/glove.6B.100d.txt',
#     ignore_case=False)  # load GloVec pre-weights
#
# inputs, embd_layer = get_embedding_layer(
#     word_dict_len=len(word_dict),
#     char_dict_len=len(char_dict),
#     max_word_len=max_word_len,
#     word_embd_dim=100,
#     char_embd_dim=50,
#     char_hidden_dim=150,
#     word_embd_weights=word_embd_weights,
#     char_hidden_layer_type='lstm')
# print("inputs: ", inputs)
# print("embd_layer: ", embd_layer)
# ###############################################################################
# # Prediction Model
# print('Create model...')
#
# ###############################################################################
# # Concatenate [MeasureEmbd, ProvisionEmbd]
# concat_input = keras.layers.concatenate([inputs, inputs])
# concat_embd = keras.layers.concatenate([embd_layer, embd_layer])
#
# lstm_layer = keras.layers.Bidirectional(
#     keras.layers.LSTM(units=50),
#     name='Bi-LSTM')(concat_embd)
#
# dense_layer = keras.layers.Dense(
#     units=2,
#     activation='softmax',
#     name='Dense')(lstm_layer)
#
# model = keras.models.Model(inputs=concat_input, outputs=dense_layer)
#
# model.compile(
#     optimizer='adam',
#     loss='categorical_crossentropy',
#     metrics=['accuracy'])
#
# model.summary()  # print model spec
#
# ###############################################################################
# # Forward Path
#
# measure_input = get_batch_input(measures,
#                                 max_word_len=max_word_len,
#                                 word_dict=word_dict,
#                                 char_dict=char_dict)
# provision_input = get_batch_input(provisions,
#                                   max_word_len=max_word_len,
#                                   word_dict=word_dict,
#                                   char_dict=char_dict)
#
# y = keras.utils.to_categorical([1], num_classes=2)
# model.fit([measure_input, provision_input], y)
# ###############################################################################
#
# # print(keras.utils.to_categorical(1))  # if 1, it's consistent
# if __name__ == "__main__":
#     pass
