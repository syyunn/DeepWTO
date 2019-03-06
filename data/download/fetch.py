""" Open pickle that holds all urls of WTO pdfs, then read and filter as to
one's necessity. """


import pickle
import os


def get_urls(ds_num):
    """
    Read urls pickle list, then give you all urls under given DS_num
    :param ds_num:
    :return: list of urls
    """
    dirname = os.path.dirname(__file__)
    print(dirname)

    with open(os.path.join(dirname, 'results/pdf_urls_parsed.pkl'), 'rb') as f:
        x = pickle.load(f)
        # print("every pdfs: ")
        # for url in x[ds_num]:
        #     print(url)
        return x[ds_num]


def filter_eng(list_of_urls):
    result = []
    print("English version of pdfs: ")
    for url in list_of_urls:
        if "Q" in url.split("/")[-4]:
            print(url)
            result.append(url)
    return result


def filter_panel_ab_eng(list_of_urls):
    """
    Filter panel/AB urls on given list of urls
    :param list_of_urls
    :return: one url that of panel report
    """
    print("Panel/AB reports: ")
    for url in list_of_urls:
        if "R" in url.split("/")[-1]:
            if "Q" in url.split("/")[-4]:
                print(url)


if __name__ == "__main__":
    ds = 202
    urls = get_urls(ds)
    filter_eng(urls)
    filter_panel_ab_eng(urls)
