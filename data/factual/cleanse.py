import re
import pickle
ds_numb = 161


factual_dict_path = "factual.pkl"
with open(factual_dict_path, 'rb') as f:
    factual_dict = pickle.load(f)

print("stored factuals: ", factual_dict.keys())

factual = factual_dict[ds_numb]

find_after_factual = [match.start() for match in re.finditer('III.', factual)]

print(find_after_factual)

print(factual[19578:])

if __name__ == "__main__":
    pass
