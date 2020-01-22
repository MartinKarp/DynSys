import numpy as np
import matplotlib.pyplot as plt
import math

steps = 11
n = steps + 1
n_p = 20000

x = np.linspace(-1,1,n_p)
y = np.arange(n)
print(y)
X, Y = np.meshgrid(x,y)

k = 0.5 * (math.sqrt(5) + 1)
for i in range(0,n-1):
    mask = X[i,:] >= 0
    X[i+1,:]= k * X[i,:] + 1
    X[i+1,mask]=  X[i+1,mask] - 2


plt.grid(True)
#plt.plot(Y[-5:,:],X[-5:,:])
plt.plot(X[0,:], X[0,:]-X[-1,:],'.')
plt.show()
