import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0,1,10)
y = np.array([0,1])
X, Y = np.meshgrid(x,y)
print(X)

X[1,:]= (5 * X[1,:]) % 1
plt.plot(X,Y)
plt.show()
