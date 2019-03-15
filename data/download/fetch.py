""" Open pickle that holds all urls of WTO pdfs, then read and filter as to
one's necessity. """

import pickle
import os

from utils.misc.yml import read_yaml

def get_urls(ds_num):
    """
    Read urls pickle list, then give you all urls under given DS_num
    :param ds_num:
    :return: list of urls
    """
    dirname = os.path.dirname(__file__)
    
    with open(os.path.join(dirname, 'results/pdf_urls_parsed.pkl'), 'rb') as f:
        x = pickle.load(f)
        print(x[ds_num])
        return x[ds_num]


def filter_eng(list_of_urls):
    result = []
    # print("English version of pdfs: ")
    for url in list_of_urls:
        if "Q" in url.split("/")[-4] or "q" in url.split("/")[-4]:
            # print(url)
            result.append(url)
    return result


def filter_panel_ab_eng(list_of_urls):
    """
    Filter panel/AB urls on given list of urls
    :param list_of_urls
    :return: one url that of panel report
    """
    mark = False
    print("Panel/AB reports: ")
    for url in list_of_urls:
        if "R" in url.split("/")[-1] or 'r' in url.split("/")[-1]:
            if "Q" in url.split("/")[-4]:
                print(url)
                mark = True
    return mark


def filter_panel_eng(list_of_urls, idx):
    """
    Filter panel report's urls on given list of urls
    :param list_of_urls
    :return: one url that of panel report
    """
    
    def _find_panel(urls, ds_idx):
        panel_url = None
        print("Panel reports: ")
        snippet = None
        for url in filter_eng(urls):
            print("url", url.split("/")[-1])
            if 'Q' in url and 'WT' in url:
                snippet = url
            
            if 'q' in url and 'WT' in url:
                snippet = url
            
            if "{}R.pdf".format(ds_idx) == url.split("/")[-1]:
                panel_url = url
                break
            
            if "{}R.PDF".format(ds_idx) == url.split("/")[-1]:
                panel_url = url
                break
            
            if "{}RW.pdf".format(ds_idx) == url.split("/")[-1]:
                panel_url = url
                break
            
            if "{}R-00.pdf".format(ds_idx) == url.split("/")[-1]:
                panel_url = url
                break
            
            if "{}R-01.pdf".format(ds_idx) == url.split("/")[-1]:
                panel_url = url
                break
                
            if not snippet:
                snippet = url
            print("urlSnippet", snippet)
            print("panel_url", panel_url)
        return panel_url, snippet
    
    panelURL, urlSNIPPET = _find_panel(list_of_urls, idx)

    if not panelURL:
        group = None
        info = read_yaml("../../data/info.yaml")
        links = info['LinkedPanel']
        for link in links:
            if idx in link:
                group = list(link.keys())
                print("group", group)
                break
        if group is not None:
            for one in group:
                print("linked", one)
                panelURL, url_snippet = _find_panel(list_of_urls, one)
                print("newly found panelURL", panelURL)
                if panelURL:
                    break
    
    if not panelURL:

        panelURL = os.path.join('/'.join(urlSNIPPET.split('/')[:-1]),
                                 '{}R.pdf'.format(idx))
        print("final_decision: ", panelURL)
    
    return panelURL

    
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
    print_urls(filter_eng(get_urls(447)))
    