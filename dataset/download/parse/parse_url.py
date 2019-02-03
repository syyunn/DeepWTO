import pickle


def split_and_filter(intermediate_str, splitter):
    """
    Split string with given splitter - either one of "," or "/'", then
    filter ones that includes "https" in oneself
    :param intermediate_str : string that in the middle of parsing
    :param splitter
    :return: chunk of string(s) as a list
    """
    intermediate_split = intermediate_str.split(splitter)
    intermediate_filter = [elem for elem in intermediate_split
                           if 'https' in elem]
    return intermediate_filter[0]


def standard_parse(string):
    """
    Parse given "a" chunk of string into valid "https:xxx.pdf" url
    :param string:
    :return:
    """
    first_output = split_and_filter(string, ",")
    second_output = split_and_filter(first_output, "\'")
    return second_output


def parse_one(string):
    result_str = standard_parse(string)
    return result_str


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
            for raw_str in result[key]:
                parsed = parse_one(raw_str)
                new_dict[key].append(parsed)
        return new_dict


if __name__ == '__main__':
    pkl_file_path = "./wto_pdf_urls.pkl"
    parsed_pkl_outpath = "./parsed.pkl"

    with open(pkl_file_path, 'rb') as f:
        result = pickle.load(f)

    parser = ParseUrl(pkl_file_path)
    parsed_dict = parser.parse_all()
    
    with open(parsed_pkl_outpath, 'wb') as f:
        pickle.dump(parsed_dict, f)
