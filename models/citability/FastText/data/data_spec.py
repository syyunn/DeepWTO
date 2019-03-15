from utils.misc.json import read_json

if __name__ == "__main__":
    read_list = read_json("Train.json")
    print(type(read_list))
    collector = set()
    for elem in read_list:
        elem = set(elem)
        
    