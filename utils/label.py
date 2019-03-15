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
