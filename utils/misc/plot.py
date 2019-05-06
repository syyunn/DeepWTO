import matplotlib.pyplot as plt


def plot2d(list_of_values, save_path=None):
    plt.plot(list_of_values)

    if save_path:
        plt.savefig(save_path)

    plt.show()