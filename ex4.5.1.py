import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-0,4,40)
y = np.linspace(-0,4,40)
X, Y = np.meshgrid(x,y)

U =  -1 * X + -1 * Y + 4
V = -X * Y + 3


u = U / np.sqrt(U**2 + V**2);
v = V / np.sqrt(U**2 + V**2);


plt.quiver(X,Y,u,v)
#plt.plot(x,4-x)
#plt.show()
