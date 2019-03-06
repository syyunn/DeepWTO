import operator

import pandas as pd
import yaml


def get_cited(csv_fp):
    """
    Read csv, returns column named "cited"
    :param csv_fp:
    :return:
    """
    df = pd.read_csv(csv_fp, skip_blank_lines=True)
    return df["cited"]


def filter_GATT(list_of_str):
    str2list = list_of_str.split("'")[1::2]
    print(str2list)
    new_list = [elem.split(".")[1].split(",") for elem in str2list
                if elem[0:4] == 'GATT']
    print(new_list)
    return new_list


def count_cited(dict_for_count, list_of_art_numb):
    """
    Input is list of article numbers in Roman, e.g.,  [' X', ' XI', ' XVIII']
    :param dict_for_count:
    :param list_of_art_numb:
    :return:
    """

    for elem in list_of_art_numb:
        if elem in dict_for_count.keys():
            dict_for_count[elem] += 1
        elif elem not in dict_for_count.keys():
            dict_for_count[elem] = 1
    return dict_for_count


def write_yaml(target_dict, filename):
    """
    Write .yaml file with key/value of target dict, with filename given.
    :param target_dict:
    :return:
    """
    with open(filename, 'w') as outfile:
        yaml.dump(target_dict, outfile, default_flow_style=False)


def sort_yaml(filename):
    """
    Sort the .yaml file in order of big value for keys
    :param filename:
    :return:
    """


def main():
    cited = dict()

    for idx, elem in enumerate(get_cited("./wto.csv")):
        cited_art_numbs = filter_GATT(get_cited("./wto.csv")[idx])
        if len(cited_art_numbs) != 0:
            cited_art_numbs = cited_art_numbs[0]
            cited = count_cited(cited, cited_art_numbs)
        else:
            pass

    write_yaml(cited, "./stat.yaml")


def sort_yaml(yaml_path):
    """
    Read yaml path then sort it by value, then print.
    :param yaml_path:
    :return: None. only prints.
    ""
    """
    stream = open(yaml_path, "r")
    docs = yaml.load_all(stream)
    result = dict()
    for doc in docs:
        for k,v in doc.items():
            result[k] = v

    sorted_result = sorted(result.items(), key=lambda kv: kv[1], reverse=True)
    print(sorted_result)


if __name__ == "__main__":
    # main()
    sort_yaml("stat.yaml")
