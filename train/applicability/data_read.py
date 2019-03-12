import pickle

from data.label.applicability.parse import cleanse_dict, invert_dict
from data.download.fetch import get_urls, filter_panel_eng

from utils.yaml import read_yaml
from utils.pdf import read_pdf
from utils.url import download

if __name__ == "__main__":
    factual_pickle = "../../data/factual/factual.pkl"
    with open(factual_pickle, 'rb') as f:
        factual_dict = pickle.load(f)
    
    gatt = read_yaml("../../data/label/applicability/labels/GATT.yaml")
    gatt = cleanse_dict(gatt)
    inv_gatt = invert_dict(gatt)
    
    # inv_keys = inv_gatt.keys()
    # for key in inv_gatt.keys():
    #     print(factual_dict[key])
    
    print(len(inv_gatt.keys()))
    print(sorted(inv_gatt.keys()))

    info = read_yaml("../../data/info.yaml")
    panel_exist = info['Panel']['ds_numb']
    
    for idx in panel_exist:
        url_to_download = filter_panel_eng(get_urls(idx))[1]
        print(url_to_download)
        break
    
    download_path = '/Users/zachary/Downloads/{}R.pdf'.format(str(idx))
    complete = download(url_to_download, download_path)

    if complete:
        read_pdf(download_path)
