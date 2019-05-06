from utils.misc.plot import plot2d

if __name__ == "__main__":
    fpath = "../../logs/sota_log.txt"
    savepath_train = "../../logs/trainLoss.png"
    savepath_test = "../../logs/testLoss.png"
    savepath_auc = "../../logs/aucroc.png"

    with open(fpath) as f:
        content = f.readlines()

    lineLength = len(content)
    print(lineLength)

    # print(content[0:100])

    count = 0
    trainLoss = []
    testLoss = []
    AUCROC = []
    for item in content:
        count += 1
        if 'All Validation set' in item:
            loss, aucroc = item.split(' ')[9], item.split(' ')[12]
            testLoss.append(float(loss))
            AUCROC.append(float(aucroc))

        if 'Train Loss' in item:
            loss = item.split(' ')[-1]
            trainLoss.append(float(loss))

    plot2d(trainLoss, savepath_train)
    plot2d(testLoss, savepath_test)
    plot2d(AUCROC, savepath_auc)

