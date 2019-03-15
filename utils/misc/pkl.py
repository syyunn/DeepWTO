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
    
    if idx == 438:
        return True # Since 438 has no factual
    
    # if idx == 476:
    #     return False
    if idx in keys:
        boolean = True
    else:
        boolean = False
    return boolean


def load_pkl(pickle_path):
    with open(pickle_path, 'rb') as f:
        py_obj = pickle.load(f)
    return py_obj


def dump_pkl(py_obj, pickle_path):
    with open(pickle_path, 'wb') as f:
        pickle.dump(py_obj, f)
    return True


if __name__ == "__main__":
    pkl_path = "../data/factual/after_panel/factual.pkl"
    with open(pkl_path, 'rb') as f:
        factual_dictionary = pickle.load(f)
    currently_stored = sorted(list(factual_dictionary.keys()))
    print(currently_stored)
    print(len(currently_stored))
    print(factual_dictionary[136])

