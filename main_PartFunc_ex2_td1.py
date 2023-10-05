import src.maths.PartialFunction as pf
import src.utils.chart_utils as cu
from matplotlib import pyplot as plt
import numpy as np


# Exercice 2 - TD1
A = [[2, np.sqrt(6)], [np.sqrt(6), 2]]
A_sdp = np.dot(np.transpose(A), A)
b = [0, 0]
c = 0
partfunc = pf.PartialFunction(A=A_sdp, b=b, c=c)

chart1 = cu.Chart(title="Fonctions partielles de la fonction F au point critique, F(x1, x2) = x1² + sqrt(6)x1x2 + x2²", xlabel="x", ylabel="y")
chart1.plot2D(nb_plots=4, type_list=[plt.plot, plt.plot, plt.plot, plt.plot], xvalues_list=[partfunc.get_x_values(), partfunc.get_x_values(), partfunc.get_x_values(), partfunc.get_x_values()], yvalues_list=[partfunc.get_y_values()[0], partfunc.get_y_values()[1], partfunc.get_y_values()[2], partfunc.get_y_values()[3]], labels_list=["e1", "e2", "v1", "v2"], save_fname="Ex2TD1_partial_functions_F_critical_point.png")


x_abs, y_abs = np.meshgrid(np.linspace(-5, 5, 101), np.linspace(-5, 5, 101))
z_abs = x_abs ** 2 + np.sqrt(6) * x_abs * y_abs + y_abs ** 2

chart2 = cu.Chart(title="Carte de niveau de la fonction F(x1, x2) = x1² + sqrt(6)x1x2 + x2²", xlabel="x", ylabel="y")
chart2.plot3D_1(type_list=[plt.contour], xvalues_list=[x_abs], yvalues_list=[y_abs], zvalues_list=[z_abs], level=100, save_fname="Ex2TD1_levels_card_100_levels.png")
chart2.plot3D_1(type_list=[plt.contour], xvalues_list=[x_abs], yvalues_list=[y_abs], zvalues_list=[z_abs], level=1000, save_fname="Ex2TD1_levels_card_1000_levels.png")

chart3 = cu.Chart(title="Représentation 3D de la surface", xlabel="x", ylabel="y")
chart3.plot3D_2(x=x_abs, y=y_abs, z=z_abs, save_fname="Ex2TD1_3D_surface.png")