###############################################################################
# This code block refers to the following link:
# https://github.com/CyberZHG/keras-word-char-embd/blob/master/keras_wc_embd/word_char_embd.py
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
###############################################################################
