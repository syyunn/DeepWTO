import pickle
from multiprocessing import Pool

from selenium import webdriver

"""

Crawls every pdf urls from WTO database and pickle the result.

"""


def get_pdf_urls(chrome_driver, dispute_idx):
    """
    Retrieve all the possible pdf urls for the given dispute number
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
            try:
                page.click()
            except: # to prevent error from unclickable element
                pass
            
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
                 start_ds_numb,
                 end_ds_numb,
                 outpath,
                 pool):
        self.chrome_driver_path = chrome_driver_path
        self.final_ds_numb = end_ds_numb
        self.start_ds_numb = start_ds_numb
        self.ds_idxs_to_crawl = [i for i in range(self.start_ds_numb,
                                                  end_ds_numb)]
        self.outpath = outpath
        self.pool = pool

        self.zeros_list = [] # for those got nothing from unstable
        # multiprocessing

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

    def update_zeros(self, output_dict):
        """
        Update self.zeros_list after verify which keys in dictionary has nothing
        :param output_dict
        :return: None (just update self.zeros_list)
        """
        keys = output_dict.keys()
        zeros_list = []
        for key in keys:
            pdf_numb = len(output_dict[key])
            if pdf_numb == 0:
                zeros_list.append(key)
        self.zeros_list = zeros_list  # update(replace) zero_list with new one!
        print("zeros_list updated: ", self.zeros_list)
        self.ds_idxs_to_crawl = zeros_list

    def crawl_idxs(self, previous_result):
        """
        Crawl all pdf links iteratively according to the list stored in the
        self.total_ds_idxs
        :type previous_result: dict
        """
        with Pool(self.pool) as p:
            try:
                crawled_result = p.map(self.unit_crawl, self.ds_idxs_to_crawl)
            except:  # to prevent chrome_driver connection error
                pass

        for d in crawled_result:
            for k, v in d.items():  # d.items() in Python 3+
                previous_result[k] = v

        return previous_result

    def crawl(self):
        """crawls all the pdf links in the WTO Database for given list of
        DS(dispute settlement) number (currently available from 1 to 577 as
        of 03 FEB 2019 """
        crawled_dict = self.crawl_idxs(dict())
        self.update_zeros(crawled_dict)
        while len(self.zeros_list) != 0:
            crawled_dict = self.crawl_idxs(crawled_dict)
            self.update_zeros(crawled_dict)

        with open(self.outpath, 'wb') as f:
            pickle.dump(crawled_dict, f)


if __name__ == "__main__":
    downloader = CrawlWTO(chrome_driver_path=
                          "/Users/jjong/Project/DeepWTO/database/chromedriver",
                          start_ds_numb=1,
                          end_ds_numb=577,
                          outpath= "/Users/jjong/Project/DeepWTO/database/"
                                   "wto_pdf_urls.pkl",
                          pool=10)

    downloader.crawl()
