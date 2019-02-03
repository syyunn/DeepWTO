import pickle
import collections
from multiprocessing import Pool


from selenium import webdriver
from tqdm import tqdm


def get_pdf_urls(chrome_driver, dispute_idx):
    """
    Retrieve all possible pdf urls for the given dispute number
    :param chrome_driver: chrome driver path
    :param dispute_idx: ds number to retrieve
    :return: string of integer
    """
    url_prefix = "https://docs.wto.org/dol2fe/Pages/FE_Search/FE_S_S006.aspx" \
                 "?Query=(@Symbol=%20wt/ds{}/*)&Language=ENGLISH&Context=" \
                 "FomerScriptedSearch&languageUIChanged=true#".\
        format(dispute_idx)
        
    chrome_driver.get(url_prefix)

    try:
        page = chrome_driver.\
            find_element_by_css_selector('#ctl00_MainPlaceHolder_dlPaging > tbody '
                                         '> tr > td:nth-child(1)')
    except:
        page = None

    page_idx = 1
    onclick_list = []
    while page:
        if page_idx != 1:
            page.click()
            
        found_elements = chrome_driver.find_elements_by_tag_name("a")
        print(len(found_elements))
        for idx in range(len(found_elements)):
            onclick = found_elements[idx].get_attribute("onclick")
            if onclick is not None and "https" in onclick:
                print(onclick)
                onclick_list.append(onclick)
       
        page_idx += 1
        try:
            page = chrome_driver.find_element_by_css_selector(
                '#ctl00_MainPlaceHolder_dlPaging > tbody > tr > td:nth-child({'
                '})'.format(page_idx))
        except:
            break
    print(len(onclick_list))
    result = dict()
    result[dispute_idx] = onclick_list
    return result

    
if __name__ == "__main__":
    chrome_driver_path = "/Users/jjong/Project/DeepWTO/download/chromedriver"
    # final_ds_numb = 577
    final_ds_numb = 3
    total_ds_idxs = [i for i in range(1, final_ds_numb)]
    n_threads = 128

    merge_dict_outpath = "/Users/jjong/Project/" \
                         "DeepWTO/download/wto_pdf_urls.pkl"


    def unit_crawl(ds_index):
        driver_one_time_use = webdriver.Chrome(chrome_driver_path)
        unit_result = get_pdf_urls(driver_one_time_use, ds_index)
        driver_one_time_use.close()
        return unit_result


    # result_dicts = []
    # for ds_idx in tqdm(total_ds_idxs):
    #     result_dict = unit_crawl(ds_idx)
    #     result_dicts.append(result_dict)

    with Pool(2) as p:
        result_dicts = p.map(unit_crawl, total_ds_idxs)

    print(result_dicts)
    print(type(result_dicts))

    merge_dict = {}
    for d in result_dicts:
        for k, v in d.items():  # d.items() in Python 3+
            merge_dict[k] = v

    # merge_dict = collections.defaultdict()
    # for d in result_dicts:
    #     for k, v in d.items():  # d.items() in Python 3+
    #         merge_dict[k].append(v)

    with open(merge_dict_outpath, 'wb') as f:
        pickle.dump(merge_dict, f)
