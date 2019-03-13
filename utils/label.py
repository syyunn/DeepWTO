import numpy as np


def index_multi_label(label_list):
    label_idx = dict()
    idx_label = dict()
    for idx, label in enumerate(label_list):
        label_idx[label] = idx
        idx_label[idx] = label
    return label_idx, idx_label


def make_one_hot(label, label_idx):
    num_label = len(list(label_idx.keys()))
    zero_hot = [0] * num_label
    for elem in label:
        idx = label_idx[elem]
        zero_hot[idx] = 1
    return zero_hot
