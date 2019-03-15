import urllib.request


def download(url, download_path):
    urllib.request.urlretrieve(url, download_path)
    return True
