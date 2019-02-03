import os
import pickle


if __name__ == '__main__':
    pkl_file_path = "./wto_pdf_urls.pkl"
    
    with open(pkl_file_path, 'rb') as f:
        pkl_f = pickle.load(f)
