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

    with open(os.path.join(dirname, 'results/pdf_urls_parsed.pkl'), 'rb') as f:
        x = pickle.load(f)
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
    mark = False
    #print("Panel/AB reports: ")
    for url in list_of_urls:
        if "R" in url.split("/")[-1] or 'r' in url.split("/")[-1]:
            if "Q" in url.split("/")[-4]:
                #print(url)
                mark = True
    return mark


def print_urls(urls):
    for url in urls:
        print(url)


if __name__ == "__main__":
    # end_ds = 511
    # total_ds = [idx for idx in range(1, 1+end_ds)]
    #
    # for idx in total_ds:
    #    urls = get_urls(idx)
    #    if filter_panel_ab_eng(urls):
    #        print(idx)
    #
    print_urls(get_urls(511))
