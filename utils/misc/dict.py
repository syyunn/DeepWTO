class Dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


def get_keys(dictionary):
    """
    :param dictionary: python dict obj
    :return: sorted list of keys of dictionary
    """
    keys = sorted(list(dictionary.keys()))
    print("length of keys: ", len(keys))
    return keys


