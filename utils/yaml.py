import yaml


def read_yaml(yaml_path):
    """
    Read yaml file from the path
    :param yaml_path:
    :return:
    """
    stream = open(yaml_path, "r")
    docs = yaml.load_all(stream)
    result = dict()
    for doc in docs:
        for k, v in doc.items():
            result[k] = v

    return result