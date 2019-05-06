if __name__ == "__main__":
    fpath = "/Users/zachary/Downloads/export_log"

    with open(fpath) as f:
        content = f.readlines()

    lineLength = len(content)
    print(lineLength)

    # print(content[0:100])

    count = 0
    for item in content:

        if 'All Validation set' in item:
            count += 1
            print(item)

    print(count)