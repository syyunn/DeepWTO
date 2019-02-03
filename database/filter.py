import pickle
from database.util import get_tail, find_panel_appellate_body_report, find_eng

if __name__ == "__main__":
    pkl_path = "./parsed.pkl"
    with open(pkl_path, "rb") as f:
        urls = pickle.load(f)

    ds_idx = 2
    
    for key in urls.keys():
        for elem in urls[key]:
            tail = get_tail(elem)
            if find_panel_appellate_body_report(tail):
                if find_eng(elem):
                    print(elem)
