from utils.yml import read_yaml
import itertools

read = read_yaml("notable.yaml")

ds_numbs = set()
titles = ['III', 'III:1', 'III:2', 'III:4', 'III:5', 'III:7']
for title in titles:
    ds_numbs = ds_numbs.union(set(read[title].split(',')))

ds_numbs = sorted(list(ds_numbs))
print(len(ds_numbs))
print(ds_numbs)

ds_numbs_wo_DS_str = []
for ds_numb in ds_numbs:
    if ' ' in ds_numb:
        ds_numb = ds_numb[1:]
        print(ds_numb)
    ds_numbs_wo_DS_str.append(int(ds_numb[2:]))

comparee = read_yaml("../../info.yaml")
comparee = comparee['Panel']['ds_numb']

joint = []
for elem in ds_numbs_wo_DS_str:
    if elem in comparee:
        joint.append(elem)

if __name__ == "__main__":
    print(sorted(set(joint)))
    print(len(sorted(set(joint))))
    pass
