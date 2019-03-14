# input

from utils.pkl import load_pkl
from utils.dict import get_keys
from utils.label import index_multi_label, make_one_hot

# Inputs
factual_path = "../../data/dataset/citability/GATT/factual.pkl"

factual = load_pkl(factual_path)
factual_keys = get_keys(factual)

# Labels
label_path = "../../data/dataset/citability/GATT/label.pkl"
label = load_pkl(label_path)
label_keys = get_keys(label)

print(label[18])

# Classes
class_path = "../../data/dataset/citability/GATT/class.pkl"
classes = load_pkl(class_path)
print(classes)
print(len(classes))

if __name__ == "__main__":
    # print(classes)
    # print(factual_keys)
    # print(label_keys)
    # print(label)
    
    # for key in factual_keys:
    #     if key in label_keys:
    #         print(factual[key])
    #         print(label[key])
    #     break
    
    label_idx, idx_label = index_multi_label(classes)
    example_label = label[18]
    one_hot = make_one_hot(example_label, label_idx)
    print(one_hot)
    print(len(one_hot))