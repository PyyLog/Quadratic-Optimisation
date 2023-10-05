import src.maths.LinearRegression as linreg
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Aircraft_Noise_Complaint_Data.csv")
df.head()
x = df[['Year']]
#print(x)
y = df[['Total Complaints']]
#print(y)
year = [2005 + i for i in range(15)]
complaints = [0 for i in range(15)]
for i in range(15):
    for j in range(len(x.values)):
        if (x.values[j] == 2005 + i):
            complaints[i] += y.values[j, 0]

print(complaints)


def X(p, q):
    o = np.size(p)
    x = np.zeros((o, 2))
    un = np.ones((o, 1))
    x[:, 0] = un
    for i in range(len(p)):
        p[:, i] = p[i]
    return x


def xTx(p, q):
    o = np.size(p)
    A = np.zeros((2, 2))
    un = np.ones((o, 1))
    A[0, 0] = 50
    A[1, 0] = np.transpose(p) @ un
    A[0, 1] = A[1, 0]
    A[1, 1] = np.linalg.norm(p) ** 2
    return A


def xTq(p, q):
    o = np.size(p)
    b = np.zeros((2, 1))
    un = np.ones((o, 1))
    b[0] = np.transpose(q) @ un
    b[1] = np.transpose(p) @ q
    return b


def f(x, y, A, b):
    a1 = A[0, 0]
    a2 = A[0, 1]
    a3 = A[1, 1]
    b1 = b[1]
    b2 = b[1]
    c = -3
    z = 0.5 * (a1 * x ** 2 + 2 * a2 * x * y + a3 * y ** 2) - (b1 * x + b2 * y) + c
    return z


#print("A (xTx) = \n", xTx(year, complaints))
#print("b (xTq) = \n", xTq(year, complaints))
A = xTx(year, complaints)
b = xTq(year, complaints)
theta = np.random.randn(2, 1)

#X_, Y_ = np.meshgrid(x_, y_)
#Z = f(X_, Y_, A, b)
#plt.contour(X_, Y_, Z, 50)

# Tracé de la régression linéaire
model = linreg.LinearRegression(learning_rate=10 ** (-3), epsilon=10 ** (-6), Nitermax=5 * (10 ** 4))
final_theta_conjugate = model.conjugate_step_gradient_descent(A, theta, b)

liste_x, liste_y = [], []

plt.figure(figsize=(15, 9))
plt.xlim(2005, 2020)
plt.ylim(-2.5 * 10e4, 3.9 * 10e5)

for i in range(len(complaints)):
    #plt.clf()
    liste_x.append(2005 + i)
    liste_y.append(complaints[i])
    plt.scatter(liste_x, liste_y, color="black")
    y_values_conjugate_step_gradient = [final_theta_conjugate[1][0] * j + final_theta_conjugate[0][0] for j in liste_y]
    plt.plot(liste_x, y_values_conjugate_step_gradient, color='red')
    plt.pause(0.002)

plt.show()