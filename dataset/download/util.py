import pickle
import re
import unittest


def verify_nonzero(pdf_urls_pkl_path):
    """
    Verify there exists no zero item with each key in given dict
    :param pdf_urls_pkl_path:
    :return: Bool
    """
    pkl_file_path = pdf_urls_pkl_path

    with open(pkl_file_path, 'rb') as f:
        result = pickle.load(f)
    
    verify_result = True
    for key in result.keys():
        if len(result[key]) == 0:
            verify_result = False
    return verify_result


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
    regex = r'^([0-9]{1,3}(R|RW)\.(pdf|PDF))|(84R-01.pdf)$'
    regex_panel = re.compile(regex)
    return regex_panel.match(tail_str)


def filter_appellate(tail_str):
    regex = r'^[0-9]{1,3}ABR\.(pdf|PDF)$'
    regex_appellate = re.compile(regex)
    return regex_appellate.match(tail_str)
