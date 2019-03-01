"""
For given DS_number,
1. Download all the pdfs in urls list from pickle
2. Read the pdf to filter the gov measure related subject - such as
"Request for Consultations" and  "Request for the Establishment of a Panel"
3. Then Concatenate filtered pdf texts
"""
import os
import urllib.request
from dataset.download.fetch_pickle import get_urls, filter_eng


def download(url):
    urllib.request.urlretrieve(url, os.path.join("downloads",
                                                 url.split("/")[-1]))


def main():
    ds_num = 161
    urls = get_urls(ds_num)
    eng_urls = filter_eng(urls)
    print(eng_urls)
    
    for eng_url in eng_urls:
        download(eng_url)


if __name__ == "__main__":
    main()
