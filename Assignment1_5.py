import numpy as np
import matplotlib.pyplot as plt

def LorentzLyapunovExp(X0, s, b, r, t, dt):
    X = X0
    v = F(X0,s,b,r)
    i = 1
    X_d = X0
    pert = 10e-6
    X_d[0] = X_d[0] + pert
    l_tot = 0
    l_old = 0

    while(True):

        X = X + dt * F(X,s,b,r)

        diff = dt * F(X_d,s,b,r)

        d = X_d + diff - X
        d2  = np.dot(d,d)
        if(d2 > 0):
            i += 1
            l_tot = l_tot + 0.5 * np.log(d2/pert**2)
            X_d = X + pert / np.sqrt(d2) * d

        if( not (i % 100000)):
            l = l_tot/(dt * i)
            print('t = ', dt * i, 'l/t = ', l, 'residual = ', l - l_old)
            l_old = l

    return l

def F( xyz, s, b, r):
    x = xyz[0]
    y = xyz[1]
    z = xyz[2]

    dx = - s * x + s * y
    dy = r * x - y - x * z
    dz = - b * z + x * y

    return np.array([dx, dy, dz])

def DF( xyz, s, b, r):
    x = xyz[0]
    y = xyz[1]
    z = xyz[2]

    dx = [- s , s, 0]
    dy = [r - z, -1, -x]
    dz = [y, x, - b]

    return np.array([dx, dy, dz])

s  =2
b = 8/3
r = 28

#s  =16
#b = 4
#r = 45.92

X0 = np.array([1,1,1])

t = 100
dt = 1e-3

L = LorentzLyapunovExp(X0, s, b, r, t, dt)
print(L)
