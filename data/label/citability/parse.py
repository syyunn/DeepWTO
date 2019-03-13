from utils.yml import read_yaml
from utils.pkl import dump_pkl
from utils.dict import get_keys


def cleanse_dict(d):
    """
    Read the yaml then Omit the 'DS' and Returns the int valued dict
    :param dict:
    :return:
    """
    new = dict()
    keys = d.keys()
    for key in keys:
        value = []
        dss = d[key].split(', ')
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


def invert_dict(dict):
    inv = {}
    for k, V in dict.items():
        for v in V:
            inv.setdefault(v, []).append(k)
    return inv


if __name__ == "__main__":
    gatt = read_yaml("labels/GATT.yaml")
    gatt = cleanse_dict(gatt)
    gatt_keys = get_keys(gatt)
    print(gatt_keys)
    inv_gatt = invert_dict(gatt)
    inv_gatt_keys = sorted(list(inv_gatt.keys()))
    print(inv_gatt)
    print(inv_gatt_keys)
    print(len(inv_gatt_keys))
    
    # Dump
    # path_to_dump = "../../dataset/citability/GATT_523/label.pkl"
    # dump_pkl(inv_gatt, path_to_dump)
    
    # Dump label keys
    path_to_dump = "../../dataset/citability/GATT_523/class.pkl"
    dump_pkl(gatt_keys, path_to_dump)
