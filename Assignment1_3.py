import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2,41)
y = np.linspace(0,2,41)
X, Y = np.meshgrid(x,y)
print(X,Y)
U =  X ** 2 * (2 * Y ** 2 - 1)
V = -Y ** 2 * (X ** 2 -1)

#plt.plot(x, x + 1/x)
#plt.plot(y**2 + 1/y, y)

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
#plt.colorbar(sm)
#plt.plot(x,4-x)
plt.show()
