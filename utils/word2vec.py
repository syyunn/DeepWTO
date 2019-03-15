import gensim.models.keyedvectors as word2vec

from utils.misc.pkl import load_pkl


def count_words(loaded_word2vec, list_of_words):
    superset = set(loaded_word2vec.vocab)
    subset = set(list_of_words)
    intersection = superset.intersection(subset)
    return len(intersection)


def binary_search(start=(2000000, 3000000),
                  criterion=13248):
    """
    Find the limit value of word2ve model that contains all criterion
    :param start:
    :param criterion:
    :return:
    """
    start = list(start)

    while start[0] != start[1]:
        limit = round((start[0] + start[1]) / 2)
        print(limit)
        model = word2vec.KeyedVectors.load_word2vec_format(
            word2vec_path, binary=True, limit=limit)
        
        inter = count_words(model, list(words_in_factual))
        print(inter)
        
        if inter == criterion:
            start[1] = limit
        elif inter < criterion:
            start[0] = limit
        print(start)
    
    print(start)
    return start


if __name__ == "__main__":
    words_in_factual = load_pkl(
        "../models/citability/FastText/data/words_in_factual.pkl")
    # print(words_in_factual)
    
    word2vec_path = "/home/ubuntu/Word2Vec/GoogleNews-vectors-negative300.bin"
    
    limit = 500000
    for i in range(6):
        limit -= 100000
        model = word2vec.KeyedVectors.load_word2vec_format(
            word2vec_path, binary=True, limit=limit)
        print("limit: {}".format(limit),
              count_words(model, words_in_factual))
