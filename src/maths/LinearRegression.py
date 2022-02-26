import numpy as np

class LinearRegression:
    def __init__(self, learning_rate, epsilon, Nitermax):
        self.learning_rate_fixed = learning_rate
        self.epsilon = epsilon
        self.Nitermax = Nitermax

    def model(self, A, theta, b):
        return np.dot(A, theta) - b

    def fixed_step_gradient(self, A, theta, b):
        return self.learning_rate_fixed * (- self.model(A, theta, b))

    def optimal_step_gradient(self, A, theta, b):
        ri = self.model(A, theta, b)
        learning_rate = (np.dot(np.transpose(ri), ri) / (np.dot(np.transpose(ri), np.dot(A, ri))))

        return learning_rate * (- self.model(A, theta, b))

    def conjugate_step_gradient(self, A, theta, b, iteration, ri_moins_1, di_moins_1):
        ri = self.model(A, theta, b)
        if iteration == 1:
            di = - self.model(A, theta, b)
            learning_rate = (np.dot(np.transpose(ri), ri) / (np.dot(np.transpose(di), np.dot(A, di))))
        else:
            beta = (np.linalg.norm(ri) ** 2) / (np.linalg.norm(ri_moins_1) ** 2)
            di = - self.model(A, theta, b) + beta * di_moins_1
            learning_rate = (np.dot(np.transpose(ri), ri) / (np.dot(np.transpose(di), np.dot(A, di))))

        return learning_rate * di

    def fixed_step_gradient_descent(self, A, theta, b):
        iteration = 0
        ri = self.model(A, theta, b)
        while (np.linalg.norm(ri) > self.epsilon) and (iteration < self.Nitermax):
            theta += self.fixed_step_gradient(A, theta, b)
            ri = self.model(A, theta, b)
            iteration += 1

        return theta

    def optimal_step_gradient_descent(self, A, theta, b):
        iteration = 0
        ri = self.model(A, theta, b)
        while (np.linalg.norm(ri) > self.epsilon) and (iteration < self.Nitermax):
            theta += self.optimal_step_gradient(A, theta, b)
            ri = self.model(A, theta, b)
            iteration += 1

        return theta

    def conjugate_step_gradient_descent(self, A, theta, b):
        iteration, ri_moins_1, di_moins_1 = 0, 0, 0
        ri = self.model(A, theta, b)
        while (np.linalg.norm(ri) > self.epsilon) and (iteration < self.Nitermax):
            theta += self.conjugate_step_gradient(A, theta, b, iteration, ri_moins_1, di_moins_1)
            ri = self.model(A, theta, b)
            di = - self.model(A, theta, b)
            ri_moins_1 = ri
            di_moins_1 = di
            iteration += 1

        return theta