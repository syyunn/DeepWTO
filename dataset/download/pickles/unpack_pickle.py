import pickle


def get_urls(ds_num):
    """
    Read urls pickle list, then give you all urls under given DS_num
    :param ds_num:
    :return: list of urls
    """

    with open('pdf_urls_parsed.pkl', 'rb') as f:
        x = pickle.load(f)
        print("every pdfs: ", x[ds_num])
        return x[ds_num]


def filter_url(list_of_urls):
    """
    Filter panel/AB urls on given list of urls
    :param list_of_urls
    :return: one url that of panel report
    """
    for url in list_of_urls:
        if "R" in url.split("/")[-1]:
            if "Q" in url.split("/")[-4]:
                print(url)


if __name__ == "__main__":
    urls = get_urls(161)
    filter_url(urls)
