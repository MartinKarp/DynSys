import numpy as np
import matplotlib.pyplot as plt

def LorentzLyapunovExp(X0):
    X = X0
    i = 0
    X_d = X0
    pert = 10e-6
    X_d[0] = X_d[0] + pert
    l_tot = 0
    l_old = 0

    while(True):

        X = F(X[0],X[1])

        d = F(X_d[0],X[1]) - X
        d2  = np.dot(d,d)
        if(d2 > 0):
            i += 1
            l_tot = l_tot + 0.5 * np.log(d2/pert**2)
            X_d = X + pert / np.sqrt(d2) * d

        if( not (i % 100000)):
            l = l_tot/(i)
            print('l/t = ', l, 'residual = ', l - l_old)
            l_old = l

    return l

a = 1.4
b = 0.3

F = lambda x, y : np.array([1 - a * x ** 2 + y, b * x])
X0 = np.zeros(2)

L = LorentzLyapunovExp(X0)
print(L)
