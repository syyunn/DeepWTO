import json


def dump_write_dict2json(dictionary, write_path):
    with open(write_path, 'w') as f:
        json.dump(dictionary, f)


def write_json_line_by_line(list_of_dicts, write_path):
    with open(write_path, "a") as outfile:
        for data in list_of_dicts[:-1]:
            json.dump(data, outfile)
            outfile.write('\n')
        json.dump(list_of_dicts[-1], outfile)


def read_json(json_path):
    with open(json_path, 'r') as f:
        lines = f.readlines()
    return lines
