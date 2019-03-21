"""
This Codes is to tokenize the given string sequence of description of
factual data.
"""

import spacy
from utils.tokenize import tokenize

# Load SpaCy model
nlp = spacy.load('en_core_web_sm')

if __name__ == "__main__":
    factual = "Korea has banned importation of steel from United States."
    
    one_dict = dict()

    keys = ["testid",
            "features_content",
            "labels_index",
            "labels_num"]

    one_dict[keys[0]] = 0
    one_dict[keys[1]] = tokenize(nlp, factual)
    one_dict[keys[2]] = [47]
    one_dict[keys[3]] = 1

    write_path = "HandWritten.json"
    with open(write_path, "a") as outfile:
        import json
        json.dump(one_dict, outfile)
        outfile.write('\n')
