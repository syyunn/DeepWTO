""" Dump the Factual Aspect of Each DS Panel Report"""

import pickle

from dataset.factual.parser import PanelParser


def main():
    ds_numb = 166
    pdf_name = "166R.pdf"
    pdf_path = "/Users/zachary/Downloads/{}".format(pdf_name)
    
    factual_dict_path = "factual.pkl"
    with open(factual_dict_path, 'rb') as f:
        factual_dict = pickle.load(f)
    
    print("stored factuals: ", factual_dict.keys())
    print("stored factual content: \n", factual_dict[ds_numb])
    
    parser = PanelParser(pdf_path)
    pdf, start, end = parser.factual_locator()
    
    print("start page idx: ", start)
    print("end page idx: ", end)
    
    factual = ''
    for page_idx in range(start, end + 1):
        print(page_idx)
        part = pdf[page_idx]
        factual += part
    # print(factual)
    factual_dict[ds_numb] = factual

    with open("factual.pkl", 'wb') as f:
        pickle.dump(factual_dict, f)


if __name__ == "__main__":
    main()
