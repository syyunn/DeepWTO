from utils.misc.yaml import read_yaml
from utils.misc.pkl import dump_pkl
from utils.misc.dict import get_keys


def cleanse_dict(dictionary):
    """
    Read the yaml then Omit the 'DS' and Returns the int-value dict with
    Article Keys
    """
    new = dict()
    keys = dictionary.keys()
    for key in keys:
        value = []
        dss = dictionary[key].split(', ')
        for ds in dss:
            num_only = int(ds[2:])
            value.append(num_only)
        new[key] = value
    return new


def assort_values(d):
    """
    Collect every values stored in dictionary, then return them as a set
    :param d:
    :return:
    """
    values = set()
    for key in d.keys():
        values |= set(d[key])
    return values


def invert_dict(dictionary):
    inv = {}
    for k, V in dictionary.items():
        for v in V:
            inv.setdefault(v, []).append(k)
    return inv


def rehash_arts_in_text(indices,
                        yaml_path=
                        "labels/GATT.yaml"):
    """
    From the integer list of labels, change the int into article name
    e/g : [0,2] -> ['Article I', 'Article II']
    """
    gatt_info = read_yaml(yaml_path)
    gatt_dict = cleanse_dict(gatt_info)
    gatt_keys_in_int = get_keys(gatt_dict)
    in_text = []
    for index in indices:
        in_text.append(gatt_keys_in_int[index])
    return in_text
    

if __name__ == "__main__":
    gatt = read_yaml("labels/GATT.yaml")
    gatt = cleanse_dict(gatt)
    print(gatt)
    gatt_keys = get_keys(gatt)
    print(gatt_keys)
    for key in gatt_keys:
        print(key)
    inv_gatt = invert_dict(gatt)
    inv_gatt_keys = sorted(list(inv_gatt.keys()))
    print(inv_gatt)
    print(inv_gatt_keys)
    print(len(inv_gatt_keys))
    
    print(rehash_arts_in_text([0, 1]))
    # Dump
    # path_to_dump = "../../dataset/citability/GATT_523/label.pkl"
    # dump_pkl(inv_gatt, path_to_dump)
    
    # Dump label keys
    # path_to_dump = "../../dataset/citability/GATT_523/class.pkl"
    # dump_pkl(gatt_keys, path_to_dump)
