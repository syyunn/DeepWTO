import time
import json
from multiprocessing import Pool

from tqdm import tqdm
from utils.misc.json import write_json_line_by_line
from utils.tokenize import tokenize

import spacy


path = "/Users/zachary/Downloads/train_data.json"

inputData = []
nlp = spacy.load('en_core_web_sm')

with open(path) as fin:
    for numline, each_line in enumerate(fin):
        unit = json.loads(each_line)
        inputData.append(unit)

print(len(inputData))


def tokenize_article(unit):
    tokens = tokenize(nlp, unit["art"])
    unit["art"] = tokens
    return unit


if __name__ == '__main__':

    def log_result(retval):
        results.append(retval)
        print('{}/{} done'.format(len(results), len(inputData)))


    pool = Pool()
    results = []
    for item in inputData:
        pool.apply_async(tokenize_article, args=[item], callback=log_result)
    pool.close()
    pool.join()
    print(results)

    write_json_line_by_line(results,
                            "/Users/zachary/Documents/train_data.json")
