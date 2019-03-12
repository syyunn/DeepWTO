import os
import pickle


def open_write_dump(pickle_path, idx, factual):
    """
    Open up pickle, read dict, add (key,value) = (idx, factual)
    :param pickle_path:
    :param idx:
    :param factual:
    :return:
    """

    if not os.path.isfile(pickle_path):
        factual_dict = dict()
        with open(pickle_path, 'wb') as f:
            pickle.dump(factual_dict, f)
    elif os.path.isfile(pickle_path):
        with open(pickle_path, 'rb') as f:
            factual_dict = pickle.load(f)
        factual_dict[idx] = factual
        with open(pickle_path, 'wb') as f:
            pickle.dump(factual_dict, f)


def check_already_exist(pickle_path, idx):
    with open(pickle_path, 'rb') as f:
        factual_dict = pickle.load(f)
    keys = factual_dict.keys()
    
    if idx in keys:
        boolean = True
    else:
        boolean = False
    return boolean


if __name__ == "__main__":
    pkl_path = "../data/factual/after_panel/factual.pkl"
    with open(pkl_path, 'rb') as f:
        factual_dictionary = pickle.load(f)
    print(factual_dictionary.keys())
    print(factual_dictionary[70])

