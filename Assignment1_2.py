import numpy as np
import matplotlib.pyplot as plt
import matplotlib

x = np.linspace(-2,2,41)
y = np.linspace(-2,2,41)
X, Y = np.meshgrid(x,y)

U =  - 1 * Y + X ** 2 * Y
V = X -  X ** 3 + Y ** 3

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
plt.plot(x,(x**3 - x)**(1/3))
plt.plot(x,-(-(x**3 - x))**(1/3))
#plt.colorbar(sm)
#plt.plot(x,4-x)
plt.show()
