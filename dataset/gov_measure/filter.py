"""
For given DS_number,
1. Download all the pdfs in urls list from pickle
2. Read the pdf to filter the gov measure related subject - such as
"Request for Consultations" and  "Request for the Establishment of a Panel"
3. Then Concatenate filtered pdf texts
"""
import os
import urllib.request

from utils.pdf import read_pdf
from dataset.download.fetch_pickle import get_urls, filter_eng


def download(url):
    download_path = os.path.join("downloads", url.split("/")[-1])
    urllib.request.urlretrieve(url, download_path)
    return download_path


def filter_gov(txt):
    tgt_phrases = ["Request for Consultations", "Request for the "
                                               "Establishment of a Panel"]
    for phrase in tgt_phrases:
        if phrase in txt:
            return True
        else:
            return False


def main():
    ds_num = 161
    urls = get_urls(ds_num)
    eng_urls = filter_eng(urls)
    print(eng_urls)
    
    gov_measure = ''
    for eng_url in eng_urls:
        fpath = download(eng_url)
        txt = read_pdf(fpath)
        boolean_mask = filter_gov(txt)
        if boolean_mask:
            gov_measure += txt
    print(txt)


if __name__ == "__main__":
    main()
