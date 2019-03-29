from utils.misc.pkl import load_pkl


if __name__ == "__main__":
    path = "class.pkl"
    classes = load_pkl(path)
    print(classes)
    print(classes[26])
