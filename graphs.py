import numpy as np
import matplotlib.pyplot as plt
from analysis import procces_results_for_graphs, sorting_names


def build_and_save_graphs(data: tuple):
    x_axis = data[0]
    y_axis = data[1]
    plt.xlim(left=2**7, right=2**15)

    for expirement in y_axis:
        for measure in y_axis[expirement]:
            for sorting in y_axis[expirement][measure]:
                plt.plot(x_axis, y_axis[expirement][measure][sorting])

            plt.legend(labels=sorting_names, loc='upper left')
            plt.xscale("log", base=2)
            plt.yscale("log")
            plt.xlabel('Array size')
            if measure == 'time':
                plt.ylabel('Execution time')
            else:
                plt.ylabel('Number of comparisons')
            plt.show()
            plt.savefig(f'expirement{expirement}_{measure}.png')
           

if __name__ == "__main__":
    data = procces_results_for_graphs('results.txt')
    print(data)
    build_and_save_graphs(data)
