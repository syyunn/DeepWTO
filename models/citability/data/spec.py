"""
This Codes are to find the statistics of token length and number of elements in
factual description in train data. Longest token length is required to pre-
determine the pad-size of input data before training.
"""

import json


def find_longest(json_data, key):
    with open(json_data) as f:
        longest = []
        for idx, each_line in enumerate(f):
            list_of_strings = json.loads(each_line)[key]
            length = len(list_of_strings)
            print(idx, length)

            if not longest:
                longest.append(length)
            elif longest[-1] < length:
                longest[-1] = length
            elif longest[-1] >= length:
                continue
        print(longest[-1])
        return longest


def find_shortest(json_data, key):
    with open(json_data) as f:
        shortest = []
        for idx, each_line in enumerate(f):
            list_of_strings = json.loads(each_line)[key]
            length = len(list_of_strings)
            print(idx, length)

            if not shortest:
                shortest.append(length)
            elif shortest[-1] > length:
                shortest[-1] = length
            elif shortest[-1] <= length:
                continue
        print(shortest[-1])
        return shortest


def find_words_set():
    collector = set()
    with open("Train.json") as f:
        for each_line in f:
            list_of_strings = json.loads(each_line)["features_content"]
            voca_set = set(list_of_strings)
            # print(voca_set)
            collector = collector.union(voca_set)
    
    print(len(collector))
    # dump_pkl(collector, "words_in_factual.pkl")
    return collector


if __name__ == "__main__":
    data_path = \
        "/home/zachary/projects/DeepWTO/models/citability_w_Article/data" \
        "/prep/entire_one_label.json"
    find_longest(data_path, 'art')

    pass
