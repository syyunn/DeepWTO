from utils.yaml import read_yaml


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
    inv_gatt = invert_dict(gatt)
    
    print(inv_gatt)
    print(inv_gatt[477])
    

