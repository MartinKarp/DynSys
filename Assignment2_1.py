import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-2,2,41)
y = np.linspace(-2,2,41)
X, Y = np.meshgrid(x,y)

U =  X - 0.25 * Y
V = Y + X * (1 - X ** 2)

y0 = np.array([0, 0])
x0 = np.array([-1, 1])

poly = np.array([1, 0, -5, 0])
for i in range(10000):
    poly[3] = 4*x0[i] + y0[i]
    r = np.roots(poly)
    r = r[np.isreal(r)]
    x0 = np.append(x0, r)
    y0 = np.append(y0,4*(r - x0[i]))

print(x0[-10:])
print(y0[-10:])
plt.plot(x0,y0,'x')

#fig1, ax1 = plt.subplots()
#ax1.plot(X, Y, '-')
#
#
#fig2, ax2 = plt.subplots()
#ax2.plot(U,V, '-')

#fig3, ax3 = plt.subplots()
#ax3.quiver(X,Y,U,V)
#plt.colorbar(sm)
#plt.plot(x,4-x)
plt.show()
