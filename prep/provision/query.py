""" Query the provision to get the target string """

import os
import re
import glob

from utils.misc.pdf import read_pdf
from utils.misc.yaml import read_yaml


def find_agreements(path_of_provisions):
    """
    Read the path and find kinds of provision, then make dictionary
    :param path_of_provisions:
    :return: dict["agreement_name"] = path
    """
    pdf_paths = glob.glob(os.path.join(path_of_provisions, "*.pdf"))
    kinds = []
    for pdf_path in pdf_paths:
        kinds.append(pdf_path.split("/")[1].split(".")[0])
    print("agreements kinds: ", kinds)
    result_dict = dict()
    for key, value in zip(kinds, pdf_paths):
        result_dict[key] = value
    return result_dict


def query(article, yaml_path):
    data = read_yaml(yaml_path)
    print(data[article])


def main():
    # provision_paths = find_agreements("pdfs")
    # print(provision_paths)
    # tgt_agreement = "GATT"
    # text = read_pdf(provision_paths[tgt_agreement])
    # print('Article III' in text)
    #
    # find = [m.start() for m in re.finditer('Article III', text)]
    # print(find)
    #
    # for start in find:
    #     print(text[start:start+1500])

    query("Article I", "gatt.yaml")

        
if __name__ == "__main__":
    main()
