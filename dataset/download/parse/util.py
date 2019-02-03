import pickle


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


def find_eng(raw_url_str):
    if 'Q' in raw_url_str:
        return True
    else:
        return False
    

def find_panel_appellate_body_report(tail_str):
    if tail_str.split('.')[0][-1] == 'R':
        return True
    else:
        return False
