import numpy as np
import matplotlib.pyplot as plt
import matplotlib

x = np.linspace(-2,2,41)
y = np.linspace(-2,2,41)
X, Y = np.meshgrid(x,y)

U =  0 * X + 1 * Y
V = X * (X * X - 1)

#amp = np.sqrt(U**2 + V**2)
#print(U.shape)
#
#norm = matplotlib.colors.Normalize()
#norm.autoscale(amp)
#cm = matplotlib.cm.copper
#
#sm = matplotlib.cm.ScalarMappable(cmap=cm, norm=norm)
#sm.set_array([])

u = U / np.sqrt(U**2 + V**2)
v = V / np.sqrt(U**2 + V**2)


#plt.quiver(X,Y,u,v, color=cm(norm(amp)))
plt.quiver(X,Y,u,v)
plt.plot(x,np.sqrt(np.abs(x**2 - 0.5 * x**4 - 1/2)))
plt.plot(x,-np.sqrt(np.abs(x**2 - 0.5 * x**4 - 1/2)))
#plt.colorbar(sm)
#plt.plot(x,4-x)
plt.show()

plt.plot(x,0.25 * x ** 4 - 0.5 * x ** 2)
