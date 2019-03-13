from utils.dict import get_keys


def check_sanity(factual, label, classes):
    """
    
    :param factual: pyDict
    :param label: pyDict
    :param label: exhaustive pyList of possible provision label
    :return:
    """
    sanity = True
    factual_keys = get_keys(factual)
    label_keys = get_keys(label)
    for key in factual_keys:
        print("key", key)
        if key in label_keys:
            print(key)
            labels = label[key]
            for label_comp in labels:
                if label_comp in classes:
                    print("okay!")
                else:
                    sanity = False
                    print("sanity check failed.")
                    return sanity

        else:
            print("the factual not in GATT label:", key)
    
    print("sanity check passes.")
    return sanity
