import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(5,10,30)
y = np.linspace(5,10,30)
X, Y = np.meshgrid(x,y)

U =  -1.5 * X + 1 * Y + 4
V = 1 * X - Y * 1


u = U / np.sqrt(U**2 + V**2);
v = V / np.sqrt(U**2 + V**2);


plt.quiver(X,Y,u,v)
#plt.plot(x,4-x)
plt.show()
