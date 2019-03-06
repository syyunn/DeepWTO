""" Extract & Dump the Factual Aspect of Each DS Panel Report into Pickle"""

import pickle
import pdftotext

from dataset.factual.parser import PanelParser


def main():
    ds_numb = 177
    pdf_name = "178R-00.pdf"
    pdf_path = "/Users/zachary/Downloads/{}".format(pdf_name)
    
    factual_dict_path = "factual.pkl"
    with open(factual_dict_path, 'rb') as f:
        factual_dict = pickle.load(f)
    
    print("stored factuals: ", factual_dict.keys())
    try:
        print("stored factual content: \n", factual_dict[ds_numb])
    except:
        print("not yet stored")
    
    # parser = PanelParser(pdf_path)
    # pdf, start, end = parser.factual_locator()
    #
    # print("start page idx: ", start)
    # print("end page idx: ", end)
    #
    # factual = ''
    # for page_idx in range(start, end + 1):
    #     print(page_idx)
    #     part = pdf[page_idx]
    #     factual += part
    # # print(factual)
    # factual_dict[ds_numb] = factual
    #
    # with open("factual.pkl", 'wb') as f:
    #     pickle.dump(factual_dict, f)


def add_annex():
    ds_numb = 177
    pdf_name = "178R-01.pdf"
    pdf_path = "/Users/zachary/Downloads/{}".format(pdf_name)
    
    factual_dict_path = "factual.pkl"
    with open(factual_dict_path, 'rb') as f:
        factual_dict = pickle.load(f)
    
    with open(pdf_path, "rb") as file:
        pdf = pdftotext.PDF(file)
    
    start = 6
    end = 14
    slice = 23600
    add = ''
    
    for page_idx in range(start, end+1):
        print(page_idx)
        page = pdf[page_idx]
        add += page

    print(add)
    print(len(add))
    print(add[:slice])
    tail_cut_add = add[:slice]

    factual_dict_path = "factual.pkl"
    with open(factual_dict_path, 'rb') as f:
        factual_dict = pickle.load(f)

    print("stored factuals: ", factual_dict.keys())
    try:
        print("stored factual content: \n", len(factual_dict[ds_numb]))
    except:
        print("not yet stored")
    
    final_facts = factual_dict[ds_numb] + tail_cut_add
    print(final_facts)
    print(len(final_facts))
    
    factual_dict[ds_numb] = final_facts
    with open("factual.pkl", 'wb') as f:
        pickle.dump(factual_dict, f)
    

if __name__ == "__main__":
    main()
    # add_annex()
