from utils.yaml import read_yaml

read = read_yaml("labels/AD.yaml")

if __name__ == "__main__":
    new = dict()
    keys = read.keys()
    for key in keys:
        value = []
        dss = read[key].split(', ')
        for ds in dss:
            numb_only = ds[2:]
            value.append(numb_only)
        new[key] = value
    print(new.keys())
    print(new['Article XXIV:12'][-1])
    
    pass
