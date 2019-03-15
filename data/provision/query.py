""" Query the provision to get the target string """

import os
import glob

from utils.misc.pdf import read_pdf


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


def main():
    provision_paths = find_agreements("./")
    tgt_agreement = "gatt"
    text = read_pdf(provision_paths[tgt_agreement])
    print(text)
    print('Article III' in text)
    idx = text.findall('Article III')
    print(idx)


if __name__ == "__main__":
    main()
