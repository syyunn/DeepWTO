from keras_wc_embd import get_dicts_generator
from utils.yaml import read_yaml

measures = read_yaml("../dataset/measure/measure.yaml")
sentence1 = measures[161]['dual retail']['RC'].split(' ')
sentence2 = measures[161]['dual retail']['REP'].split(' ')


sentences = [
    sentence1,
    sentence2,
]

dict_generator = get_dicts_generator(
    word_min_freq=1,
    char_min_freq=1,
    word_ignore_case=False,
    char_ignore_case=False,
)
for sentence in sentences:
    dict_generator(sentence)

word_dict, char_dict, max_word_len = dict_generator(return_dict=True)

if __name__ == "__main__":
    print(measures)
    print(sentence1)
    print(sentence2)
    print(word_dict)
    print(char_dict)
    print(max_word_len)
