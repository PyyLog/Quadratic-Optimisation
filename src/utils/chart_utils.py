from matplotlib import pyplot as plt
import mpl_toolkits.mplot3d as plt3D
import itertools


class Chart:
    def __init__(self, title, xlabel, ylabel):
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.colors = ["white", "red", "green", "orange", "gold", "lime", "navy", "black", "purple", "magenta", "cyan", "salmon", "pink", "deepskyble", "lawngreen", "grey", "dimgray"]

    def set_black_background(self):
        plt.style.use("dark_background")

        for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
            plt.rcParams[param] = '0.9'  # very light grey

        for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
            plt.rcParams[param] = '#212946'  # bluish dark grey

    def glowing_lines(self, nb_plots, type_list, xvalues_list, yvalues_list):
        n_shades = 10
        diff_linewidth = 1.05
        alpha_value = 0.3 / n_shades

        for n in range(1, n_shades + 1):
            for i, j in itertools.zip_longest(range(nb_plots), range(nb_plots), fillvalue=""):
                type_list[j](xvalues_list[j], yvalues_list[j], linewidth=2 + (diff_linewidth * n), alpha=alpha_value, color=self.colors[j])

    def plot2D(self, nb_plots, type_list, xvalues_list, yvalues_list, labels_list, save_fname):
        self.set_black_background()
        plt.figure(figsize=(15, 9))
        for i, j in itertools.zip_longest(range(nb_plots), range(nb_plots), fillvalue=""):
            type_list[j](xvalues_list[j], yvalues_list[j], label=labels_list[j], color=self.colors[j])

        self.glowing_lines(nb_plots, type_list, xvalues_list, yvalues_list)
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.legend()
        plt.grid()
        plt.savefig(save_fname)
        plt.show()

    def plot3D_1(self, type_list, xvalues_list, yvalues_list, zvalues_list, level, save_fname):
        plt.style.use("default")
        plt.figure(figsize=(15, 9))
        for i, j in itertools.zip_longest(range(1), range(1), fillvalue=""):
            type_list[j](xvalues_list[j], yvalues_list[j], zvalues_list[j], level)

        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.legend()
        plt.grid()
        plt.savefig(save_fname)
        plt.show()

    def plot3D_2(self, x, y, z, save_fname):
        fig = plt.figure(figsize=(15, 9))
        ax = fig.gca(projection='3d')
        proj_3D = ax.plot_surface(x, y, z, cmap=plt.cm.coolwarm, linewidth=2, antialiased=False)
        ax.zaxis.set_major_locator(plt.LinearLocator(5))
        ax.zaxis.set_major_formatter(plt.FormatStrFormatter('%.02f'))
        fig.colorbar(proj_3D, shrink=0.5, aspect=5)
        plt.savefig(save_fname)
        plt.show()
