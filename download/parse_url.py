import pickle

if __name__ == "__main__":
    path = "./wto_pdf_urls.pkl"
    with open(path, 'rb') as f:
        pkl_f = pickle.load(f)
        print(pkl_f.keys())
        print(pkl_f)
        print(pkl_f[1])
        print(len(pkl_f[1]))

        print(pkl_f[2])
        print(len(pkl_f[2]))
