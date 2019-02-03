import pickle
from multiprocessing import Pool


from selenium import webdriver


def get_pdf_urls(chrome_driver, dispute_idx):
    """
    Retrieve all possible pdf urls for the given dispute number
    :param chrome_driver: chrome driver path
    :param dispute_idx: ds number to retrieve
    :return: string of integer
    """
    url_prefix = "https://docs.wto.org/dol2fe/Pages/FE_Search/" \
                 "FE_S_S006.aspx?Query=(@Symbol=%20wt/ds{}/*)&" \
                 "Language=ENGLISH&Context=FomerScriptedSearch&" \
                 "languageUIChanged=true#".format(dispute_idx)
        
    chrome_driver.get(url_prefix)

    try:
        page = chrome_driver.\
            find_element_by_css_selector('#ctl00_MainPlaceHolder_dlPaging '
                                         '> tbody > tr > td:nth-child(1)')
    except:  # to prevent the case where wrong final ds_number is given
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
                '#ctl00_MainPlaceHolder_dlPaging > tbody '
                '> tr > td:nth-child({})'.format(page_idx))
        except:  # to escape after every pages has been visited
            break
    print(len(onclick_list))
    result = dict()
    result[dispute_idx] = onclick_list
    return result


class CrawlWTO:
    """
    Visit every ds_number of pages database then crawl all the pdf urls
    """
    def __init__(self,
                 chrome_driver_path,
                 final_ds_numb,
                 outpath,
                 pool):
        self.chrome_driver_path = chrome_driver_path
        self.final_ds_numb = final_ds_numb
        self.total_ds_idxs = [i for i in range(1, final_ds_numb)]
        self.outpath = outpath
        self.pool = pool

    def unit_crawl(self, ds_index):
        """
        Unit crawler to be used in multiprocessing
        :param ds_index
        :return: dictionary that contains every pdf urls with ds_idx as key
        """
        driver_one_time_use = webdriver.Chrome(self.chrome_driver_path)
        unit_result = get_pdf_urls(driver_one_time_use, ds_index)
        driver_one_time_use.close()
        return unit_result

    def crawl(self):
        with Pool(self.pool) as p:
            result_dicts = p.map(self.unit_crawl, self.total_ds_idxs)
    
        print(result_dicts)
        print(type(result_dicts))
    
        merge_dict = {}
        for d in result_dicts:
            for k, v in d.items():  # d.items() in Python 3+
                merge_dict[k] = v
    
        with open(self.outpath, 'wb') as f:
            pickle.dump(merge_dict, f)

    
if __name__ == "__main__":
    downloader = CrawlWTO(chrome_driver_path=
                          "/Users/zachary/projects/DeepWTO/database"
                          "/chromedriver",
                          final_ds_numb=577,
                          outpath= "/Users/zachary/projects/DeepWTO/database/"
                                   "wto_pdf_urls.pkl",
                          pool=30)

    downloader.crawl()
