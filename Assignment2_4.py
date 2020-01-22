import numpy as np
import matplotlib.pyplot as plt
a = 1.4
b = 0.3
n = int(1e4)
eps = 10 ** - np.linspace(0.1,2,4)
print(eps)
xy = np.zeros([n+1,2])
f = lambda x, y : np.array([1 - a * x ** 2 + y, b * x])


for i in range(n):
    xy[i+1,:] =f(xy[i,0], xy[i,1])

boxes = np.zeros(eps.shape)

for i,w in enumerate(eps):
    y_g = np.linspace(-0.4, 0.4, int(2 * 0.4 / eps[i]))
    x_g = np.linspace(-1.4, 1.4, int( 2 * 1.4 / eps[i]))

    X, Y = np.meshgrid(x_g,y_g)
    X = X.ravel()
    Y = Y.ravel()
    for j,w2 in enumerate(X):
        for k,w3 in enumerate(xy):
            if(abs(xy[k,0]-X[j]) < eps[i]/2 and abs(xy[k,1] - Y[j]) < eps[i]/2):
                boxes[i] += 1
                break
plt.loglog(1/eps,boxes,'x')
l_box = np.log(boxes)
l_eps = np.log(1/eps)
print(boxes)
print(l_box)
print(l_eps)
p = np.polyfit(l_eps, l_box, 1)
print(p)
plt.loglog(1/eps,1/eps ** p[0]*np.exp(p[1]))







#plt.plot(xy[:,0],xy[:,1], 'x')
