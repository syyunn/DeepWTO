from data.label.applicability.parse import cleanse_dict, invert_dict
from data.download.fetch import get_urls, filter_panel_eng

from utils.misc.yml import read_yaml
from utils.misc.url import download
from utils.misc.pkl import open_write_dump, check_already_exist

from data.factual.after_panel.extract import extract_factual_manual, locate_chapter_II, locate_chapter_III


def read_label(idx):
    gatt = read_yaml("../../data/label/applicability/labels/GATT.yaml")
    gatt = cleanse_dict(gatt)
    inv_gatt = invert_dict(gatt)
    
    print(len(inv_gatt.keys()))
    print(sorted(inv_gatt.keys()))
    return inv_gatt[idx]


if __name__ == "__main__":
    pkl_path = "../../data/factual/after_panel/factual.pkl"
    info = read_yaml("../../data/info.yaml")
    panel_exist = info['Panel']['ds_numb']
    mutual_agree = info['Panel']['mutual_agree']
    WPF = info['Panel']['WPF']
    print(WPF)
    LinkedPanel = info['LinkedPanel']
    LinkedOmit = info['LinkedOmit']
    for idx in panel_exist:
        if check_already_exist(pkl_path, idx):
            continue
        elif idx in mutual_agree:
            continue
        elif idx in WPF:
            print(idx, "in WPF")
            continue
        elif idx in LinkedOmit:
            print(idx, "in LinkedOmit")
            continue
        else:
            print("processing: DS", idx)
            url_to_download = filter_panel_eng(get_urls(idx), idx)
            print(url_to_download)

            download_path = '/Users/zachary/Downloads/{}R.pdf'.format(str(idx))
            complete = download(url_to_download, download_path)
            
            # complete = True
        
            if complete:
                # factual = extract_factual_auto(download_path)
                factual = extract_factual_manual(download_path)
                # print(factual)
                
                before_pos = locate_chapter_II(factual)
                after_pos = locate_chapter_III(factual)
                
                factual = factual[before_pos:after_pos]
                
                print(factual)
                
                open_write_dump(pkl_path, idx, factual)
    
            elif not complete:
                print("download_fail for: ", idx)
        break
