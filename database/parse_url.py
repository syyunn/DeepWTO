def split_and_filter(intermediate_str, splitter):
    """
    Split string with given splitter - either one of "," or "/'", then
    filter ones that includes "https" in oneself
    :param intermediate_str : string that in the middle of parsing
    :param splitter
    :return: chunk of string(s) as a list
    """
    intermediate_split = intermediate_str.split(splitter)
    intermediate_filter = [elem for elem in intermediate_split if 'https' in elem]
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


class ParseUrl:
    def __init__(self, string):
        self.string = string

    def parse(self):
        result_str = standard_parse(self.string)
        return result_str


if __name__ == '__main__':
    # pkl_file_path = "./wto_pdf_urls.pkl"
    #
    # with open(pkl_file_path, 'rb') as f:
    #     pkl_f = pickle.load(f)

    example = ["var w=window.open('https://docs.wto.org/dol2fe/Pages/FE_Search/DDFDocuments/4255/Q/WT/DS/2-10A7.pdf','downloadFile', 'directories=1, height= 100, location=0, menubar=0, resizable=0, scrollbars=1, status=1, toolbar=0, width= 200', true, 720, 600);w.focus(); return false;"]

    

    result = standard_parse(example[0])
    print(result)
