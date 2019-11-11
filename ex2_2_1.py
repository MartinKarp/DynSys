import numpy as np
import matplotlib.pyplot as plt

# %% a.

A = np.array([[6, -3],[2,1]])
x = np.linspace(-5,5,10)
X, Y = np.meshgrid(x,x,indexing='ij')

u =  A[0,0] * X + A[0,1] * Y
v =  A[1,0] * X + A[1,1] * Y

plt.quiver(X,Y,u,v)

# %% b
A = np.array([[-2, 1],[-4,3]])
x = np.linspace(-5,5,10)
X, Y = np.meshgrid(x,x,indexing='ij')

u =  A[0,0] * X + A[0,1] * Y
v =  A[1,0] * X + A[1,1] * Y

plt.quiver(X,Y,u,v)

# %% c
A = np.array([[-4, 1],[-1,-2]])
x = np.linspace(-5,5,10)
X, Y = np.meshgrid(x,x,indexing='ij')

u =  A[0,0] * X + A[0,1] * Y
v =  A[1,0] * X + A[1,1] * Y

plt.quiver(X,Y,u,v)

# %% d
A = np.array([[0, -1],[1,0]])
x = np.linspace(-5,5,10)
X, Y = np.meshgrid(x,x,indexing='ij')

u =  A[0,0] * X + A[0,1] * Y
v =  A[1,0] * X + A[1,1] * Y

plt.quiver(X,Y,u,v)
# %% e
A = -1 * np.array([[0, -1],[1,0]])
x = np.linspace(-5,5,10)
X, Y = np.meshgrid(x,x,indexing='ij')

u =  A[0,0] * X + A[0,1] * Y
v =  A[1,0] * X + A[1,1] * Y

plt.quiver(X,Y,u,v)

# %% f
A = np.array([[5, -5],[2,-1]])
x = np.linspace(-5,5,10)
X, Y = np.meshgrid(x,x,indexing='ij')

u =  A[0,0] * X + A[0,1] * Y
v =  A[1,0] * X + A[1,1] * Y

plt.quiver(X,Y,u,v)
# %% g
A = np.array([[1, -2],[3,-4]])
x = np.linspace(-5,5,10)
X, Y = np.meshgrid(x,x,indexing='ij')

u =  A[0,0] * X + A[0,1] * Y
v =  A[1,0] * X + A[1,1] * Y

plt.quiver(X,Y,u,v)
