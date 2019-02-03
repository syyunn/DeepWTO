import pickle
import re


def get_tail(raw_url_str):
    """
    Get final end chunk of https url - such as "https:1/2/3/4.pdf
    => returns 4.pdf
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
    regex = r'^([0-9]{1,3}(R|RW)\.(pdf|PDF))|(84R-01.pdf)|(135R-00.pdf)$'
    regex_panel = re.compile(regex)
    return regex_panel.match(tail_str)


def filter_appellate(tail_str):
    regex = r'^[0-9]{1,3}ABR\.(pdf|PDF)$'
    regex_appellate = re.compile(regex)
    return regex_appellate.match(tail_str)


def extract_number(str_chunk):
    return int(re.search(r'\d+', str_chunk).group())


if __name__ == "__main__":
    pkl_path = "./pdf_urls_parsed.pkl"
    with open(pkl_path, "rb") as f:
        urls = pickle.load(f)

    AB_list = []
    Panel_list = []
    linked_tuples_panel = []
    linked_tuples_appellate = []
    for key in urls.keys():
        for elem in urls[key]:
            print(key)
            print(elem)
            tail = get_tail(elem)
            if filter_english(elem):
                print(elem)
                if filter_panel(tail):
                    print(tail)
                    Panel_list.append(key)
                    given = extract_number(tail.split('.')[0])
                    if given != key:
                        linked_tuples_panel.append((key, given))
                if filter_appellate(tail):
                    print(tail)
                    AB_list.append(key)
                    given = extract_number(tail.split('.')[0])
                    if given != key:
                        linked_tuples_appellate.append((key, given))

        if key == 135:
            break
    AB_list = sorted(list(set(AB_list)))
    Panel_list = sorted(list(set(Panel_list)))

    # Panel list includes AB_list
    for elem in AB_list:
        if elem not in Panel_list:
            print(elem)
            print("error!")

    print(AB_list)
    print(Panel_list)

    print(len(AB_list))
    print(len(Panel_list))

    print(linked_tuples_panel)
    print(linked_tuples_appellate)