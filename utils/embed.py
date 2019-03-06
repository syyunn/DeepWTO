import numpy

import keras
import codecs

###############################################################################
# This code block refers to the following link:
# https://github.com/CyberZHG/keras-word-char-embd/blob/master/keras_wc_embd/
# word_char_embd.py
# written by CyberZHG


def get_dicts_generator(word_min_freq=4,
                        char_min_freq=2,
                        word_ignore_case=False,
                        char_ignore_case=False):
    """Get word and character dictionaries from sentences.

    :param word_min_freq: The minimum frequency of a word.
    :param char_min_freq: The minimum frequency of a character.
    :param word_ignore_case: Word will be transformed to lower case before
    saving to dictionary.
    :param char_ignore_case: Character will be transformed to lower case before
    saving to dictionary.
    :return gen: A closure that accepts sentences and returns the dictionaries.
    """
    word_count, char_count = {}, {}

    def get_dicts(sentence=None,
                  return_dict=False):
        """Update and return dictionaries for each sentence.

        :param sentence: A list of strings representing the sentence.
        :param return_dict: Returns the dictionaries if it is True.
        :return word_dict, char_dict, max_word_len:
        """
        if sentence is not None:
            for word in sentence:
                if not word:
                    continue
                if word_ignore_case:
                    word_key = word.lower()
                else:
                    word_key = word
                word_count[word_key] = word_count.get(word_key, 0) + 1
                for char in word:
                    if char_ignore_case:
                        char_key = char.lower()
                    else:
                        char_key = char
                    char_count[char_key] = char_count.get(char_key, 0) + 1
        if not return_dict:
            return None
        word_dict, char_dict = {'': 0, '<UNK>': 1}, {'': 0, '<UNK>': 1}
        max_word_len = 0
        for word, count in word_count.items():
            if count >= word_min_freq:
                word_dict[word] = len(word_dict)
                max_word_len = max(max_word_len, len(word))
        for char, count in char_count.items():
            if count >= char_min_freq:
                char_dict[char] = len(char_dict)
        return word_dict, char_dict, max_word_len

    return get_dicts


def get_embedding_weights_from_file(word_dict, file_path, ignore_case=False):
    """Load pre-trained embeddings from a text file.

    Each line in the file should look like this:
        word feature_dim_1 feature_dim_2 ... feature_dim_n

    The `feature_dim_i` should be a floating point number.

    :param word_dict: A dict that maps words to indice.
    :param file_path: The location of the text file containing the pre-trained
    embeddings.
    :param ignore_case: Whether ignoring the case of the words.

    :return weights: A numpy array.
    """
    pre_trained = {}
    with codecs.open(file_path, 'r', 'utf8') as reader:
        for line in reader:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if ignore_case:
                parts[0] = parts[0].lower()
            pre_trained[parts[0]] = list(map(float, parts[1:]))
    embd_dim = len(next(iter(pre_trained.values())))
    weights = [[0.0] * embd_dim for _ in range(max(word_dict.values()) + 1)]
    for word, index in word_dict.items():
        if not word:
            continue
        if ignore_case:
            word = word.lower()
        if word in pre_trained:
            weights[index] = pre_trained[word]
        else:
            weights[index] = numpy.random.random((embd_dim,)).tolist()
    return numpy.asarray(weights)


def get_char_hidden_layer(char_dict_len,
                          max_word_len,
                          char_hidden_dim=150,
                          char_hidden_layer_type='lstm'):
    """Get the merged embedding layer.
    :param char_dict_len: The number of characters in the dictionary including
    the ones mapped to 0 or 1.
    :param max_word_len: The maximum allowed length of word.
    :param char_hidden_dim: The dimensions of the hidden states of RNN in one
    direction.
    :param char_hidden_layer_type: The type of the recurrent layer, 'lstm' or
    'gru'.

    :return inputs, embd_layer: The keras layer.
    """
    if char_hidden_layer_type == 'lstm':
        char_hidden_layer = keras.layers.Bidirectional(
            keras.layers.LSTM(
                units=char_hidden_dim,
                input_shape=(max_word_len, char_dict_len),
                return_sequences=False,
                return_state=False,
            ),
            name='Bi-LSTM_Char',
        )
    elif char_hidden_layer_type == 'gru':
        char_hidden_layer = keras.layers.Bidirectional(
            keras.layers.GRU(
                units=char_hidden_dim,
                input_shape=(max_word_len, char_dict_len),
                return_sequences=False,
                return_state=False,
            ),
            name='Bi-GRU_Char',
        )
    elif char_hidden_layer_type == 'cnn':
        char_hidden_layer = [
            keras.layers.Conv1D(
                filters=max(1, char_hidden_dim // 5),
                kernel_size=3,
                activation='relu',
            ),
            keras.layers.Flatten(),
            keras.layers.Dense(
                units=char_hidden_dim,
                name='Dense_Char',
            ),
        ]
    elif isinstance(char_hidden_layer_type, list) or \
            isinstance(char_hidden_layer_type, keras.layers.Layer):
        char_hidden_layer = char_hidden_layer_type
    else:
        raise NotImplementedError('Unknown character hidden layer type: %s'
                                  % char_hidden_layer_type)
    if not isinstance(char_hidden_layer, list):
        char_hidden_layer = [char_hidden_layer]
    return char_hidden_layer
###############################################################################
