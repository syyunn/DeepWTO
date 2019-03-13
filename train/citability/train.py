# input

from utils.pkl import load_pkl
from utils.dict import get_keys

factual_path = "../../data/dataset/citability/GATT_523/factual.pkl"

factual = load_pkl(factual_path)
factual_keys = get_keys(factual)

if __name__ == "__main__":
    print(factual_keys)
