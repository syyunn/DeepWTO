""" Dump the Factual Aspect of Each DS Panel Report"""

import pickle

from dataset.factual.parser import PanelParser


def main():
    ds_numb = 162
    path = "/Users/zachary/Downloads/162R-00.pdf"
    factual_dict = {}
    parser = PanelParser(path)
    pdf, start, end = parser.factual_locator()
    
    factual = ''
    for page_idx in range(start, end + 1):
        print(page_idx)
        part = pdf[page_idx]
        factual += part
    print(factual)
    factual_dict[ds_numb] = factual
    
    with open("factual.pkl", 'wb') as f:
        pickle.dump(factual_dict, f)


if __name__ == "__main__":
    main()
