"""
Split entire data set into train/test in balanced way of labels
"""
import os
import numpy as np
import json
import random

from utils.misc.json import write_json_line_by_line


def count_total(entire_data):
    """
    Get entire json and return how many lines it holds.
    """
    num_lines = sum(1 for line in open(entire_data))

    return num_lines


def split(entire_data, test_mask):
    count = 0
    train_dicts = []
    test_dicts = []
    with open(entire_data) as fin:
        for each_line in fin:
            each_line = json.loads(each_line)
            if count in test_mask:
                test_dicts.append(each_line)
            else:
                train_dicts.append(each_line)
            count += 1
    return train_dicts, test_dicts


def locate_label_one_and_zero(json_file):
    with open(json_file) as fin:
        count = 0
        label_one = 0
        label_one_idx = []
        label_zero_idxs = []
        label_one_idxs = []
        for line_idx, each_line in enumerate(fin):
            count += 1
            data = json.loads(each_line)
            # print(data)
            # print(data.keys())
            if data['label'] == [1]:
                label_one += 1
                label_one_idxs.append(line_idx)
            else:
                label_zero_idxs.append(line_idx)
                
        print("num total test data: {}".format(count))
        print("num total label [1]: {}".format(label_one))
    return label_one_idxs, label_zero_idxs


def split_random_w_ratio(mylist, ratio):
    len_mylist = len(mylist)
    mylist = np.array(mylist)
    mask = sorted(random.sample(range(len_mylist),
                  int(len_mylist * ratio)))
    not_mask = [i for i in range(len_mylist) if i not in mask]
    
    l1 = mylist[not_mask]
    l2 = mylist[mask]
    
    return list(l1), list(l2)


if __name__ == "__main__":
    entire_data_path = "../test_data.json"
    one_idxs, zero_idxs = locate_label_one_and_zero(entire_data_path)
    print(one_idxs)
    print(len(one_idxs))
    print(len(zero_idxs))

    # entire_data_path = "entire_one_label.json"
    # one_idxs, zero_idxs = locate_label_one_and_zero(entire_data_path)
    # print(one_idxs)
    # print(len(one_idxs))
    # print(len(zero_idxs))
    #
    # ratio = 0.2
    # mask_ones_train, mask_ones_test = split_random_w_ratio(one_idxs, ratio)
    # print(len(mask_ones_train))
    # print(len(mask_ones_test))
    # mask_zeros_train, mask_zeros_test = split_random_w_ratio(
    # zero_idxs, ratio)
    # print(len(mask_zeros_train))
    # print(len(mask_zeros_test))
    #
    # mask_train = mask_ones_train + mask_zeros_train
    # print(mask_train)
    # mask_test = mask_ones_test + mask_zeros_test
    #
    # print(len(mask_train))
    # print(len(mask_test))
    #
    # assert len(set(mask_train).intersection(set(mask_test))) == 0
    #
    # train, test = split(entire_data_path, mask_test)
    #
    # # Delete pre-exist data (because of 'a', this process required)
    # write_train_data_path = "../train_data.json"
    # write_test_data_path = "../test_data.json"
    #
    # if os.path.isfile(write_train_data_path):
    #     os.remove(write_train_data_path)
    # if os.path.isfile(write_test_data_path):
    #     os.remove(write_test_data_path)
    #
    # write_json_line_by_line(train, "../train_data.json")
    # write_json_line_by_line(test, "../test_data.json")
    #
    # print(count_total("../train_data.json"))
    # print(count_total("../test_data.json"))

    pass
