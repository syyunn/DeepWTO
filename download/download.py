import os
import re

import wget
from selenium import webdriver


def get_pdf_url(chrome_driver, dispute_idx):
    """
    Retrieve pdf url of given dispute number
    :param chrome_driver: chrome driver path
    :param dispute_idx: ds number to retrieve
    :return: string of integer
    """
    url_prefix = "https://docs.wto.org/dol2fe/Pages/FE_Search/FE_S_S006.aspx" \
                 "?Query=(@Symbol=%20wt/ds{}/*)&Language=ENGLISH&Context=" \
                 "FomerScriptedSearch&languageUIChanged=true#".\
        format(dispute_idx)
    
    chrome_driver.get(url_prefix)
    
    possible_tr_idx = 2
    pdf_urls = []
    for index in range(possible_tr_idx):
        common_xpath = '//*[@id="ctl00_MainPlaceHolder_dtlDocs"]/tbody/tr[{}' \
                       ']/td/div/div[3]/div[5]/a'.format(index+1)
        
        found_elements = driver.find_elements_by_xpath(common_xpath)
        
        common_url_prefix = 'https'
        common_url_postfix = 'pdf'
        
        try:
            to_be_parsed = found_elements[0].get_attribute("onclick")
        
            start_of_url_string_index = re.search(common_url_prefix,
                                                  to_be_parsed).start()
            end_of_url_string_index = re.search(common_url_postfix,
                                                to_be_parsed).end()

            pdf_url = to_be_parsed[
                      start_of_url_string_index:end_of_url_string_index]
    
            pdf_urls.append(pdf_url)
    
        except (AttributeError, IndexError):
            pass
    return pdf_urls
    
    
def check_panel_report(url):
    """
    Check the validity of url whether the url directs the panel report or else.
    :return: Bool
    """
    try:
        int(url.split('/')[-1].split('.')[0][:-1])
        if url.split('/')[-1].split('.')[0][-1] == 'R':
            return True
        else:
            return False
    except (ValueError, AttributeError):
        return False
    
    
def download_panel_report(resume_idx,
                          total_disputes,
                          root_dir,
                          chrome_driver):
    panel_report_exists = []
    panel_report_not_exists = []
    for dispute_idx in range(resume_idx, total_disputes):
        urls = get_pdf_url(chrome_driver, dispute_idx)
        for url in urls:
            is_panel_report = check_panel_report(url)
            print(is_panel_report)
            print(dispute_idx, url)
            if is_panel_report:
                outpath = os.path.join(root_dir, str(dispute_idx) + "R.pdf")
                print(outpath)
                wget.download(url, outpath)
                panel_report_exists.append(dispute_idx)
            else:
                panel_report_not_exists.append(dispute_idx)

            
if __name__ == "__main__":
    chrome_driver_path = "/Users/zachary/projects/" \
                         "DeepWTO/download/chromedriver"
    driver = webdriver.Chrome(chrome_driver_path)
    
    total_numb_ds = 577
    download_root = "/Users/zachary/projects/DeepWTO/download/panel_reports"
    resume_number = 1
    download_panel_report(resume_number,
                          total_numb_ds+1,
                          download_root,
                          driver)
    
    # with tr[1]"
    # 7
    # R.pdf
    # 12
    # R.pdf
    # 14
    # R.pdf
    # 72
    # R.pdf
    # 323
    # R.pdf
    # 391
    # R.pdf