import numpy as np


class PartialFunction:
    def __init__(self, A, b, c):
        self.A = A
        self.b = b
        self.c = c

    def get_eigenvalues(self):
        return np.linalg.eig(self.A)[0]

    def get_eigenvectors(self):
        return np.linalg.eig(self.A)[1]

    def get_x_asterisk(self):
        return np.linalg.solve(self.A, self.b)

    def get_fx_asterisk(self):
        x_asterisk = self.get_x_asterisk()
        first_term = (1 / 2) * np.dot(np.dot(np.transpose(x_asterisk), self.A), x_asterisk)
        second_term = - np.dot(np.transpose(self.b), x_asterisk)
        third_term = self.c
        fx_asterisk = first_term + second_term + third_term

        return fx_asterisk

    def get_partial_function(self, vect, i):
        first_term = np.dot(np.dot(np.transpose(vect), self.A), vect) * (i ** 2)
        fx_asterisk = self.get_fx_asterisk()
        fxd = (1 / 2) * first_term + fx_asterisk

        return fxd

    def get_x_values(self):
        return [i for i in np.arange(-5, 5, 10 ** (-2))]

    def get_y_values(self):
        fxe1_list, fxe2_list, fxv1_list, fxv2_list = [], [], [], []

        e1 = [1, 0]
        e2 = [0, 1]
        vectv1 = self.get_eigenvectors()[:, 0]
        vectv2 = self.get_eigenvectors()[:, 1]

        for i in np.arange(-5, 5, 10 ** (-2)):
            fxe1_list.append(self.get_partial_function(e1, i))
            fxe2_list.append(self.get_partial_function(e2, i))
            fxv1_list.append(self.get_partial_function(vectv1, i))
            fxv2_list.append(self.get_partial_function(vectv2, i))

        return fxe1_list, fxe2_list, fxv1_list, fxv2_list

    def get_level_card_function(self, xx1, xx2):
        return 2 * xx1 ** 2 + 2 * xx1 * xx2 + xx2 ** 2 - 3
