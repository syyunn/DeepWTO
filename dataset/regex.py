import unittest
import re

regex_panel = re.compile(r'^[0-9]{1,3}(R|RW)\.pdf$')
regex_appellate = re.compile(r'^[0-9]{1,3}ABR\.pdf$')

regex = r'^({}\.(pdf|PDF))|(84R-01.pdf)$'.format(10)
regex_arg = re.compile(regex)

regex_eng = re.compile(r'^(.*)(\/q\/|\/Q\/)(.*)$')


class TestRE(unittest.TestCase):
    
    def test_int(self):
        self.assertTrue(regex_panel.match('110R.pdf'))
        self.assertTrue(regex_appellate.match('123ABR.pdf'))
        self.assertTrue(regex_arg.match('10.pdf'))
        self.assertTrue(regex_eng.match("https://docs.wto.org/dol2fe/Pages/FE_Search/DDFDocuments/250742/q/WT/DS/574-1.pdf"))
        self.assertTrue(regex_eng.match("https://docs.wto.org/dol2fe/Pages/FE_Search/DDFDocuments/250742/Q/WT/DS/574-1.pdf"))
        self.assertFalse(regex_eng.match("https://docs.wto.org/dol2fe/Pages/FE_Search/DDFDocuments/250742/r/WT/DS/574-1.pdf"))
        



