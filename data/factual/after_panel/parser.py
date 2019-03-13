""" Parse and Extract the Factual Aspects from the given Panel Report"""

import re
import pdftotext
# brew install pkg-config poppler to "pip install pdftotext" on mac


class PanelParser:
    def __init__(self, filepath):
        with open(filepath, "rb") as file:
            pdf = pdftotext.PDF(file)
        self.pdf = pdf
        
    def factual_locator(self):
        romans = ["I.", "II.", "III.", "IV.", "V.", "VI.", "VII.", "VIII.",
                  "IX.", "X."]
        # romans = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII",
        #           "IX", "X"]
        
        pdf_all = "\n\n".join(self.pdf)
        contents = re.findall('(.*?)[\W]+(\d+)(?=\n|$)', pdf_all, flags=re.M)
        # print(contents)

        page_of_factual_aspect = None
        roman_idx_of_factual_aspect = None
        
        for idx, content in enumerate(contents):
            # print(content)
            for elem in content:
                if ("FACTUAL" in elem) or ("Factual" in elem) or \
                        ("CHRONOLOGY OF EVENTS" in elem):
                    # print(elem)
                    page_of_factual_aspect = int(content[1])
                    print("FACTUAL ASPECT IS AT PAGE {}".
                          format(page_of_factual_aspect))
                    roman_idx_of_factual_aspect = content[0].split(" ")[0]
                    print("ROMAN OF FACTUAL ASPECT IS {}".
                          format(roman_idx_of_factual_aspect))
                    for roman_idx, roman in enumerate(romans):
                        if roman == roman_idx_of_factual_aspect:
                            next_roman = romans[roman_idx+1]
                            next_next_roman = romans[roman_idx+2]
                            print("next_roman (to mark the finish): ",
                                  next_roman)
                if page_of_factual_aspect and roman_idx_of_factual_aspect:
                    break
                else:
                    continue
            else:
                continue
            break
        previous_page = []
        for content in contents:
            previous_page.append(content[1])
            for elem in content:
                # print(elem)
                
                manual = True
                if manual:
                    next_roman = str(1)
                    next_next_roman = str(1)
                    print("next_roman and next_next_roman not located")
                
                if next_roman in elem:
                    page_of_factual_aspect_end = int(content[1])
                    print("FACTUAL ASPECT IS AT PAGE {}".
                          format(page_of_factual_aspect_end))
                    break
                elif next_next_roman in elem:
                    page_of_factual_aspect_end = int(previous_page[-2])
                else:
                    continue
                break
            else:
                continue
            break

        digital_pdf_idx_of_factual_aspect = None
        digital_pdf_idx_of_factual_aspect_end = None
        for idx in range(0, len(self.pdf)):
            if "Page {}".format(page_of_factual_aspect) in self.pdf[idx]:
                # print("Page {}".format(page_of_factual_aspect))
                digital_pdf_idx_of_factual_aspect = idx
                print("digital_pdf_idx_of_factual_aspect",
                      digital_pdf_idx_of_factual_aspect)
                break

        for idx in range(0, len(self.pdf)):
            if "Page {}".format(page_of_factual_aspect_end) in self.pdf[idx]:
                digital_pdf_idx_of_factual_aspect_end = idx
                print("digital_pdf_idx_of_factual_aspect_end",
                      digital_pdf_idx_of_factual_aspect_end)
                break
                
        if digital_pdf_idx_of_factual_aspect and \
                    digital_pdf_idx_of_factual_aspect_end:
                print("all found")
            
        # print(self.pdf[digital_pdf_idx_of_factual_aspect])
        # print(self.pdf[digital_pdf_idx_of_factual_aspect_end])
        
        return self.pdf, \
            digital_pdf_idx_of_factual_aspect,\
            digital_pdf_idx_of_factual_aspect_end
       

def main():
    path = "/Users/zachary/Downloads/166R.pdf"
    parser = PanelParser(path)
    parser.factual_locator()


if __name__ == "__main__":
    main()

