"""
For given DS_number,
1. Download all the pdfs in urls list from pickle
2. Read the pdf to filter the gov measure related subject - such as
"Request for Consultations" and  "Request for the Establishment of a Panel"
3. Then Concatenate filtered pdf texts
"""
import os
import urllib.request
from multiprocessing import Pool

from utils.pdf import read_pdf
from dataset.download.fetch_pickle import get_urls, filter_eng


def download(url):
    download_path = os.path.join("downloads", url.split("/")[-1])
    urllib.request.urlretrieve(url, download_path)
    return download_path


def filter_gov(txt):
    tgt_phrases = ["Request for Consultations",
                   "Request for the Establishment of a Panel"]
    bools = []
    for phrase in tgt_phrases:
        if phrase in txt:
            bools.append(True)
    if True in bools:
        return True
    else:
        return False


def unit_filter(url):
    fpath = download(url)
    txt = read_pdf(fpath)
    boolean_mask = filter_gov(txt)
    if boolean_mask:
        return txt
    else:
        return ''


def multiprocess_filter(pool_number, urls):
    with Pool(pool_number) as p:
        texts = p.map(unit_filter, urls)
    count = 0
    gov_measure = ''
    for text in texts:
        gov_measure += text
        if text != '':
            count += 1

    print(gov_measure)
    print(count)
    
    return gov_measure


def main():
    ds_num = 161
    urls = get_urls(ds_num)
    eng_urls = filter_eng(urls)
    pool_num = 20
    multiprocess_filter(pool_num, eng_urls)


if __name__ == "__main__":
    main()
