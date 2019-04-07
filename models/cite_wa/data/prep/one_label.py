"""Convert Multi Label Dataset to One-Label"""

import os
import json
from utils.misc.yaml import read_yaml
from utils.misc.dict import get_keys
from utils.misc.json import write_json_line_by_line

from prep.label.cite.parse import cleanse_dict

print(os.getcwd())

multi_label_json = "entire_data.json"
provision_path = "/home/zachary/projects/DeepWTO/data/provision/gatt.yaml"
provision = read_yaml(provision_path)

provision_names = list(provision.keys())
print(provision_names)
print(len(provision_names))
print(provision[provision_names[0]])


gatt = read_yaml("/home/zachary/projects/DeepWTO/data/label/citability/labels"
                 "/GATT.yaml")
gatt = cleanse_dict(gatt)
gatt_keys = get_keys(gatt)
print(gatt_keys)
art_id = gatt_keys.index("Article I")
print(art_id)

print(provision_names == gatt_keys)

num_class = len(provision_names)
dicts_to_write_in_json = []
with open(multi_label_json) as fin:
    for each_line in fin:
        data = json.loads(each_line)
        # print(data)
        # print(data.keys())
        # print(data['labels_index'])
        for art_id in range(num_class):
            dict_to_write = dict()

            dict_to_write['testid'] = str(data['testid']) \
                                      + "_[{}]"\
                                          .format(provision_names[art_id])
            dict_to_write['gov'] = data['features_content']
            dict_to_write['art'] = provision[provision_names[art_id]]
            dict_to_write['label'] = [1] if art_id in data['labels_index'] \
                else [0]
            # print(dict_to_write)
            # print(dict_to_write['label'])
            # print(dict_to_write['gov'])
            dicts_to_write_in_json.append(dict_to_write)

print(len(dicts_to_write_in_json))

path_to_write = os.path.join(os.getcwd(), "entire_one_label.json")
print(path_to_write)

os.remove(path_to_write)

write_json_line_by_line(dicts_to_write_in_json, path_to_write)
        
if __name__ == "__main__":
    pass

