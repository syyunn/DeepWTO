""" Parse the downloaded urls to make individually downloadable"""

import pickle


def split_and_filter(intermediate_str, splitter):
    """
    Split string with given splitter - practically either one of "," or "/'".
    Then filter ones that includes "https" in the split pickles
    :param intermediate_str : string that in the middle of parsing
    :param splitter
    :return: chunk of string(s) as a list
    """
    intermediate_split = intermediate_str.split(splitter)
    intermediate_filter = [elem for elem in intermediate_split
                           if 'https' in elem]
    return intermediate_filter[0]


def parse_one(string):
    """
    Parse and filter given chunk of string into "https:xxx.pdf" url format.
    Apply split_and_filter for two times in a row.
    :param string:
    :return: "https:xxx.pdf"
    """
    first_output = split_and_filter(string, ",")
    second_output = split_and_filter(first_output, "\'")
    return second_output


def parse_mutliple_documents(string):
    """
    Split multiple urls embedded in one url - which looks as following:
    "https://docs.wto.org/dol2fe/Pages/FE_Search/MultiDDFDocuments/44321/S/WT/
    DS/135R-00.pdf;S/WT/DS/135R-01.pdf;S/WT/DS/135R-02.pdf/"
    :param string:
    :return: Multiple urls
    """
    def clean_backslash_at_the_back(url):
        if url[-1] == '/':
            cleaned_url_string = url[:-1]
            return cleaned_url_string
        else:
            return url
    
    def replace_MultiDDFDocuments(url):
        """
        Replace the part of url "MultiDDFDocuments" to "DDFDocuments"
        :param url:
        :return:
        """
        target = url.split('/')
        if "MultiDDFDocuments" in target:
            idx = target.index("MultiDDFDocuments")
            target[idx] = "DDFDocuments"
        newly_made_url = "/".join(target)
        return newly_made_url
    
    if ';' in string:
        multiple_chunks = string.split(';')
        chunks = multiple_chunks[0]
        chunks_split = chunks.split("/")[:-1]
        MultiDDF_idx = chunks_split.index("MultiDDFDocuments")
        chunks_split[MultiDDF_idx] = "DDFDocuments"
        reference = "/".join(chunks_split)
        return_list = []
        for postfix_with_QWTDS in multiple_chunks:
            postfix = postfix_with_QWTDS.split("/")[-1]
            new_url = "/".join([reference, postfix])
            back_cleaned_url = clean_backslash_at_the_back(new_url)
            multidoc_replaced_url = replace_MultiDDFDocuments(back_cleaned_url)
            return_list.append(multidoc_replaced_url)
        return return_list
    else:
        return [string]

        
class ParseUrl:
    """
    Parse the raw string crawled and extract valid 'https:xxx.pdf'
    """
    def __init__(self, pkl_path):
        
        with open(pkl_path, 'rb') as f:
            self.target = pickle.load(f)
    
    def parse_all(self):
        new_dict = dict()
        for key in self.target.keys():
            new_dict[key] = []

            for raw_str in self.target[key]:
                parsed = parse_one(raw_str)
                new_dict[key].append(parsed)
            
            new_value = []
            for parsed_str in new_dict[key]:
                semicolon_parsed_list = parse_mutliple_documents(parsed_str)
                new_value += semicolon_parsed_list
            new_dict[key] = new_value
            
        return new_dict
    
    
if __name__ == '__main__':
    pkl_file_path = "./pickles/pdf_urls_raw.pkl"
    parsed_pkl_outpath = "./pickles/pdf_urls_parsed.pkl"

    parser = ParseUrl(pkl_file_path)
    parsed_dict = parser.parse_all()

    with open(parsed_pkl_outpath, 'wb') as f:
        pickle.dump(parsed_dict, f)
