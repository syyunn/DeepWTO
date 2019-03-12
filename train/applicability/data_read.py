import pickle

from data.label.applicability.parse import cleanse_dict, invert_dict
from utils.yaml import read_yaml

if __name__ == "__main__":
    factual_pickle = "../../data/factual/factual.pkl"
    with open(factual_pickle, 'rb') as f:
        factual_dict = pickle.load(f)
    
    gatt = read_yaml("../../data/label/applicability/labels/GATT.yaml")
    gatt = cleanse_dict(gatt)
    inv_gatt = invert_dict(gatt)
    
    # inv_keys = inv_gatt.keys()
    # for key in inv_gatt.keys():
    #     print(factual_dict[key])
    
    print(len(inv_gatt.keys()))
