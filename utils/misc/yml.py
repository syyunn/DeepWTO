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
#
# def check_linked():


if __name__ == "__main__":
    info = read_yaml("../data/info.yaml")
    LinkedPanel = info['LinkedPanel']
    
    print(LinkedPanel)
    
    to_omit = []
    for elem in LinkedPanel:
        links = sorted(list(elem.keys()))
        print(links)
        to_omit += links[1:]
    print(to_omit)
