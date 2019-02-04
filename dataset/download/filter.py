import pickle
import re

import yaml

with open("../info.yaml", 'r') as stream:
    info_yaml = yaml.load(stream)


def get_tail(raw_url_str):
    """
    Get final end chunk of https url- such as, for given "https:1/2/3/4.pdf,
    returns "4.pdf"
    :param raw_url_str: str
    :return: str
    """
    split = raw_url_str.split('/')
    if len(split[-1]) == 0:  # in case there's appended '/' at the end of url
        return split[-2]
    else:
        return split[-1]


def filter_english(raw_url_str):
    regex_eng = re.compile(r'^(.*)(\/q\/|\/Q\/)(.*)$')
    return regex_eng.match(raw_url_str)


def filter_panel(tail_str):
    def generate_regex_for_multidoc_case():
        multidoc_keys_type1 = info_yaml["MultiplePanelReport"]["type1"]
        multidoc_keys_type2 = info_yaml["MultiplePanelReport"]["type2"]

        regex = r'^([0-9]{1,3}(R|RW)\.(pdf|PDF))'
        commmon_str_type_1 = '|({}R-00.pdf)'
        commmon_str_type_2 = '|({}R-01.pdf)'
        for multidoc_key_type1 in multidoc_keys_type1:
            regex += commmon_str_type_1.format(multidoc_key_type1)
        for multidoc_key_type2 in multidoc_keys_type2:
            regex += commmon_str_type_2.format(multidoc_key_type2)
        regex += '$'
        return regex
    regex_panel = generate_regex_for_multidoc_case()
    regex_panel = re.compile(regex_panel)
    return regex_panel.match(tail_str)


def filter_appellate(tail_str):
    regex = r'^[0-9]{1,3}ABR\.(pdf|PDF)$'
    regex_appellate = re.compile(regex)
    return regex_appellate.match(tail_str)


def extract_number(str_chunk):
    return int(re.search(r'\d+', str_chunk).group())


def parse_linked_cases(sample):
    length = len(sample)
    search_idx = 0
    while search_idx < length-1:
        element = sample[search_idx]
        next_elem = sample[search_idx+1]
        if element.intersection(next_elem):
            sample[search_idx] = element.union(next_elem)
            del sample[search_idx+1]
            length = len(sample)
        else:
            search_idx += 1
    return sample


if __name__ == "__main__":
    pkl_path = "./result/pdf_urls_new_parsed.pkl"
    with open(pkl_path, "rb") as f:
        urls = pickle.load(f)

    AB_list = []
    Panel_list = []
    linked_tuples_panel = []
    linked_tuples_appellate = []
    for key in urls.keys():
        print(key)

        for elem in urls[key]:
            print(elem)
            tail = get_tail(elem)
            print(tail)
            if filter_english(elem):
                print(elem)
                if filter_panel(tail):
                    print(tail)
                    Panel_list.append(key)
                    given = extract_number(tail.split('.')[0])
                    if given != key:
                        linked_tuples_panel.append({key, given})
                if filter_appellate(tail):
                    print(tail)
                    AB_list.append(key)
                    given = extract_number(tail.split('.')[0])
                    if given != key:
                        linked_tuples_appellate.append({key, given})

        if key == 379:
            pass
    AB_list = sorted(list(set(AB_list)))
    Panel_list = sorted(list(set(Panel_list)))

    # Panel list includes AB_list
    multidoc_list = []
    for elem in AB_list:
        if elem not in Panel_list:
            print(elem)
            print("error!")
            multidoc_list.append(elem)

    print(AB_list)
    print(Panel_list)

    print(len(AB_list))
    print(len(Panel_list))

    print(linked_tuples_panel)
    # print(linked_tuples_appellate)

    # print(multidoc_list)
    
    print(parse_linked_cases(linked_tuples_panel))
    print(parse_linked_cases(linked_tuples_appellate))