import PyPDF2


def read_pdf(path):
    """
    Read the given path of pdf file, return the PdfFileReader_Object
    :param path: str
    :return: str
    """
    file = open(path, 'rb')
    pdf = PyPDF2.PdfFileReader(file)
    num_pages = pdf.numPages
    txt = ''
    for page_idx in range(num_pages):
        page_obj = pdf.getPage(page_idx)
        page_txt = page_obj.extractText()
        txt += page_txt
    return txt

