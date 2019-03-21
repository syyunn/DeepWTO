import spacy

from utils.misc.pkl import load_pkl
from utils.misc.dict import get_keys

from utils.label import index_multi_label, get_label_idx

# # Inputs
# factual_path = "../data/dataset/citability/GATT/factual.pkl"
# factual = load_pkl(factual_path)
# factual_keys = get_keys(factual)
#
# # Labels
# label_path = "../data/dataset/citability/GATT/label.pkl"
# label = load_pkl(label_path)
# label_keys = get_keys(label)
#
# # Classes
# class_path = "../data/dataset/citability/GATT/class.pkl"
# classes = load_pkl(class_path)
# label2idx, idx2label = index_multi_label(classes)
#
# Load SpaCy model
nlp = spacy.load('en_core_web_sm')


def tokenize(nlp_model, str2tokenize):
    doc = nlp_model(str2tokenize)
    token_bag = []
    for token in doc:
        token_bag.append(str(token))
    return token_bag


def make_input(factual_dict, labels_dict):
    inputs = []
    
    input_data_keys = ["testid",
                       "features_content",
                       "labels_index",
                       "labels_num"]
    
    factual_dict_keys = get_keys(factual_dict)
    
    for ds_number in factual_dict_keys:
        if ds_number in label_keys:
            temporal_dict = dict()
            temporal_dict[input_data_keys[0]] = ds_number
            temporal_dict[input_data_keys[1]] = tokenize(nlp,
                                                         factual_dict[
                                                             ds_number])
            label_idxs = get_label_idx(labels_dict[ds_number], label2idx)
            temporal_dict[input_data_keys[2]] = label_idxs
            temporal_dict[input_data_keys[3]] = len(label_idxs)
            inputs.append(temporal_dict)
        else:
            continue
    return inputs


if __name__ == "__main__":
    input_data = make_input(factual, label)
    write_path = "../train/citability/FastText/data/data.json"
    with open(write_path, "a") as outfile:
        import json
        for data in input_data[:-1]:
            json.dump(data, outfile)
            outfile.write('\n')
        json.dump(input_data[-1], outfile)
    pass
