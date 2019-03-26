"""
This Codes is to tokenize the given string sequence of description of
factual data.
"""

import spacy
from utils.tokenize import tokenize
from utils.misc.json import write_json_one_line


def do_tokenize(factual, id=0, label=[0]):
    """
    Perform Tokenize to make input data dict.
    In case you perform test, just set id and label arbitrarily.
    It does not affect the result.
    """
    # Load SpaCy model
    nlp = spacy.load('en_core_web_sm')
    
    one_dict = dict()

    keys = ["testid",
            "features_content",
            "labels_index",
            "labels_num"]

    one_dict[keys[0]] = id  # id
    one_dict[keys[1]] = tokenize(nlp, factual)
    one_dict[keys[2]] = label
    one_dict[keys[3]] = len(label)
    
    return one_dict


if __name__ == "__main__":
    factual_text = "Korea has banned importation of beef from United States!"
    data_input = do_tokenize(factual_text)
    print(data_input)
    
    # Write Out the input
    write_path = "test_data.json"
    write_json_one_line(write_path, data_input)
