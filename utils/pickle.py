import os
import pickle


def open_write_dump(pkl_path, idx, factual):
    """
    Open up pickle, read dict, add (key,value) = (idx, factual)
    :param pkl_path:
    :param idx:
    :param factual:
    :return:
    """

    if not os.path.isfile(pkl_path):
        factual_dict = dict()
        with open(pkl_path, 'wb') as f:
            pickle.dump(factual_dict, f)
    elif os.path.isfile(pkl_path):
        with open(pkl_path, 'rb') as f:
            factual_dict = pickle.load(f)
        factual_dict[idx] = factual
        with open(pkl_path, 'wb') as f:
            pickle.dump(factual_dict, f)
