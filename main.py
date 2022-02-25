import LinearRegression as lr
import time
import numpy as np
from matplotlib import pyplot as plt
import src.utils.chart_utils as cu

model = lr.LinearRegression(learning_rate=10 ** (-3), epsilon=10 ** (-6), Nitermax=5 * (10 ** 4))
chart = cu.Chart("Distribution de la taille par rapport à l'âge", xlabel="Age", ylabel="Taille")
p, q = [np.loadtxt("src/datas/dataP.dat")], [np.loadtxt("src/datas/dataQ.dat")]

x = np.reshape(p[0], (np.shape(p[0])[0], 1))
y = np.reshape(q[0], (np.shape(q[0])[0], 1))
A = np.concatenate((np.ones(np.shape(x)), x), axis=1)
A_sdp = np.dot(np.transpose(A), A)
b = np.dot(np.transpose(A), y)
theta = np.random.randn(2, 1)

fixed_start_time = time.time()
final_theta_fixed = model.fixed_step_gradient_descent(A_sdp, theta, b)
fixed_end_time = time.time()

optimal_start_time = time.time()
final_theta_optimal = model.optimal_step_gradient_descent(A_sdp, theta, b)
optimal_end_time = time.time()

conjugate_start_time = time.time()
final_theta_conjugate = model.conjugate_step_gradient_descent(A_sdp, theta, b)
conjugate_end_time = time.time()

print("Durée de réalisation de la méthode du gradient à pas fixe : ", fixed_end_time - fixed_start_time, "sec.")
print("Durée de réalisation de la méthode du gradient à pas optimal : ", optimal_end_time - optimal_start_time, "sec.")
print("Durée de réalisation de la méthode du gradient à pas conjugué : ", conjugate_end_time - conjugate_start_time, "sec.")

y_values_fixed_step_gradient = [final_theta_fixed[1][0] * i + final_theta_fixed[0][0] for i in p[0]]
y_values_optimal_step_gradient = [final_theta_optimal[1][0] * i + final_theta_optimal[0][0] for i in p[0]]
y_values_conjugate_step_gradient = [final_theta_conjugate[1][0] * i + final_theta_conjugate[0][0] for i in p[0]]

chart.plot(nb_plots=2, type_list=[plt.scatter, plt.plot], list_xvalues=[p, p[0]], list_yvalues=[q, y_values_fixed_step_gradient], list_labels=[None, "Pas fixe"])
chart.plot(nb_plots=2, type_list=[plt.scatter, plt.plot], list_xvalues=[p, p[0]], list_yvalues=[q, y_values_optimal_step_gradient], list_labels=[None, "Pas optimal"])
chart.plot(nb_plots=2, type_list=[plt.scatter, plt.plot], list_xvalues=[p, p[0]], list_yvalues=[q, y_values_conjugate_step_gradient], list_labels=[None, "Pas conjugué"])
