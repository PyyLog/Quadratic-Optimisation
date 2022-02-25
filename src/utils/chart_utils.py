from matplotlib import pyplot as plt
import itertools


class Chart:
    def __init__(self, title, xlabel, ylabel):
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel

    def plot(self, nb_plots, type_list, list_xvalues, list_yvalues, list_labels):
        plt.figure(figsize=(15, 9))
        for i, j in itertools.zip_longest(range(nb_plots), range(nb_plots), fillvalue=""):
            type_list[j](list_xvalues[j], list_yvalues[j], label=list_labels[j])

        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.legend()
        plt.grid()
        plt.show()
