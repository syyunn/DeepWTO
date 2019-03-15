def index_multi_label(label_list):
    label2idx = dict()
    idx2label = dict()
    for idx, label in enumerate(label_list):
        label2idx[label] = idx
        idx2label[idx] = label
    return label2idx, idx2label


def make_one_hot(label, label2idx):
    num_label = len(list(label2idx.keys()))
    zero_hot = [0] * num_label
    for elem in label:
        idx = label2idx[elem]
        zero_hot[idx] = 1
    return zero_hot


def get_label_idx(label, label2idx):
    return_list = []
    for elem in label:
        return_list.append(label2idx[elem])
    return return_list


if __name__ == "__main__":
    # input
    from utils.misc.pkl import load_pkl
    from utils.misc.dict import get_keys
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
