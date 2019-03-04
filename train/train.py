import os
import random

import numpy as np

import keras
from keras_wc_embd import get_dicts_generator, get_embedding_layer, \
    get_batch_input, get_embedding_weights_from_file

from utils.yaml import read_yaml

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

word_embd_weights = get_embedding_weights_from_file(
    word_dict,
    'GloVec/glove.6B.300d.txt',
    ignore_case=False)  # load GloVec pre-weights

inputs, embd_layer = get_embedding_layer(
    word_dict_len=len(word_dict),
    char_dict_len=len(char_dict),
    max_word_len=max_word_len,
    word_embd_dim=300,
    char_embd_dim=50,
    char_hidden_dim=150,
    word_embd_weights=word_embd_weights,
    char_hidden_layer_type='lstm'
)
print("inputs: ", inputs)
###############################################################################
# Prediction Model
print('Create model...')

# Concatenate [MeasureEmbd, ProvisionEmbd]
concat_embedding = keras.layers.Concatenate(
    name='EmbeddingMeasureProvision')([embd_layer, embd_layer])

lstm_layer = keras.layers.Bidirectional(
    keras.layers.LSTM(units=50),
    name='Bi-LSTM',
)(concat_embedding)

dense_layer = keras.layers.Dense(
    units=2,
    activation='softmax',
    name='Dense',
)(lstm_layer)

model = keras.models.Model(inputs=inputs, outputs=dense_layer)

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy'])

model.summary()  # print model spec


###############################################################################


def train_batch_generator():
    while True:
        measure_input = get_batch_input(measures,
                                        max_word_len=max_word_len,
                                        word_dict=word_dict,
                                        char_dict=char_dict)
        provision_input = get_batch_input(provisions,
                                          max_word_len=max_word_len,
                                          word_dict=word_dict,
                                          char_dict=char_dict)
        yield np.array([measure_input, provision_input]), \
              keras.utils.to_categorical([1])


###############################################################################
# Forward Path

model.fit_generator(
    generator=train_batch_generator(),
    steps_per_epoch=1,
    epochs=1,
    verbose=True)

###############################################################################

if __name__ == "__main__":
    pass
