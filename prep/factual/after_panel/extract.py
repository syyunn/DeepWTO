""" Extract & Dump the Factual Aspect of Each DS Panel Report into Pickle"""

import pickle

from data.factual.after_panel.parser import PanelParser


def extract_factual_auto(pdf_path):
    """
    Extract "II. Factual Aspect" from the given path of PDF
    :param pdf_path: local path of PanelReport.pdf
    :return: strings of "II. Factual Aspect"
    """

    parser = PanelParser(pdf_path)
    pdf, start, end = parser.factual_locator()

    print("start page idx: ", start)
    print("end page idx: ", end)

    factual = ''
    for page_idx in range(start, end + 1):
        print(page_idx)
        part = pdf[page_idx]
        factual += part
    return factual
    
    
def extract_factual_manual(pdf_path):
    """
    Extract "II. Factual Aspect" from the given path of PDF
    :param pdf_path: local path of PanelReport.pdf
    :return: strings of "II. Factual Aspect"
    """
    parser = PanelParser(pdf_path)
    pdf, start, end = parser.factual_locator()

    start = 16
    end = 16
    
    factual = ''
    for page_idx in range(start, end + 1):
        print(page_idx)
        part = pdf[page_idx]
        factual += part
    return factual


def locate_chapter_II(factual):
    import re
    pos_of_before_factual = [match.start() for match in
                          re.finditer('\n2 ', factual)]
    
    print(pos_of_before_factual)
    return pos_of_before_factual[0]


def locate_chapter_III(factual):
    import re
    # print(factual)
    pos_of_after_factual = [match.start() for match in
                            re.finditer('\n3 ', factual)]
    
    print(pos_of_after_factual)
    return pos_of_after_factual[0]


def main():
    ds_numb = 244
    multi_doc = True
    manual = True
    if not multi_doc:
        pdf_name = "{}R.pdf".format(ds_numb)
    elif multi_doc:
        pdf_name = "{}R-00.pdf".format(ds_numb)
    
    pdf_path = "/Users/zachary/Downloads/{}".format(pdf_name)
    
    factual_dict_path = "factual.pkl"
    with open(factual_dict_path, 'rb') as f:
        factual_dict = pickle.load(f)
    
    print("stored factuals: ", factual_dict.keys())
    try:
        print("stored factual content: \n", factual_dict[ds_numb])
    except:
        print("not yet stored")
        
    parser = PanelParser(pdf_path)
    pdf, start, end = parser.factual_locator()

    print("start page idx: ", start)
    print("end page idx: ", end)

    factual = ''
    
    if not manual:
        for page_idx in range(start, end + 1):
            print(page_idx)
            part = pdf[page_idx]
            factual += part
        factual_dict[ds_numb] = factual
        
    elif manual:
        start = 11
        end = 11
        for page_idx in range(start, end + 1):
            print(page_idx)
            part = pdf[page_idx]
            factual += part
        factual_dict[ds_numb] = factual

    with open("factual.pkl", 'wb') as f:
        pickle.dump(factual_dict, f)


# def add_annex():
#     ds_numb = 177
#     pdf_name = "178R-01.pdf"
#     pdf_path = "/Users/zachary/Downloads/{}".format(pdf_name)
#
#     factual_dict_path = "factual.pkl"
#     with open(factual_dict_path, 'rb') as f:
#         factual_dict = pickle.load(f)
#
#     with open(pdf_path, "rb") as file:
#         pdf = pdftotext.PDF(file)
#
#     start = 6
#     end = 14
#     slice = 23600
#     add = ''
#
#     for page_idx in range(start, end+1):
#         print(page_idx)
#         page = pdf[page_idx]
#         add += page
#
#     print(add)
#     print(len(add))
#     print(add[:slice])
#     tail_cut_add = add[:slice]
#
#     factual_dict_path = "factual.pkl"
#     with open(factual_dict_path, 'rb') as f:
#         factual_dict = pickle.load(f)
#
#     print("stored factuals: ", factual_dict.keys())
#     try:
#         print("stored factual content: \n", len(factual_dict[ds_numb]))
#     except:
#         print("not yet stored")
#
#     final_facts = factual_dict[ds_numb] + tail_cut_add
#     print(final_facts)
#     print(len(final_facts))
#
#     factual_dict[ds_numb] = final_facts
#     with open("factual.pkl", 'wb') as f:
#         pickle.dump(factual_dict, f)
    

if __name__ == "__main__":
    main()
    # add_annex()
