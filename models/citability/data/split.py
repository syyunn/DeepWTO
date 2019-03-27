"""
Split entire data set into train/test
"""
import os
import random

from utils.misc.json import write_json_line_by_line


def count_total(entire_data):
    """
    Get entire json and return how many lines it holds.
    """
    num_lines = sum(1 for line in open(entire_data))

    return num_lines


def split(entire_data, _test_mask):
    count = 0
    train_dicts = []
    test_dicts = []
    with open(entire_data) as fin:
        for each_line in fin:
            if count in _test_mask:
                train_dicts.append(each_line)
            else:
                test_dicts.append(each_line)
            count += 1
    return train_dicts, test_dicts
    
    
if __name__ == "__main__":
    entire_data_path = "entire_data.json"
    total_count = count_total(entire_data_path)
    print(total_count)

    test_proportion = 0.1
    test_mask = sorted(random.sample(range(total_count),
                                     int(total_count * 0.1)))
    print(test_mask)

    train, test = split(entire_data_path, test_mask)
    
    # Delete pre-exist data (because of 'a', this process required)
    write_train_data_path = "train_data.json"
    write_test_data_path = "test_data.json"
    os.remove(write_train_data_path)
    os.remove(write_test_data_path)
    
    write_json_line_by_line(train, "train_data.json")
    write_json_line_by_line(test, "test_data.json")
    
    print(count_total("train_data.json"))
    print(count_total("test_data.json"))

    pass
