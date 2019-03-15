import json


def dump_write_dict2json(dictionary, write_path):
    with open(write_path, 'w') as f:
        json.dump(dictionary, f)
