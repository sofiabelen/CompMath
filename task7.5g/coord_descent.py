import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np

def f(x, y):
    return x**3 + 8 * y**3 -6 * x * y + 1

A = 0
B = 1

def coord_descent():
    x0, y0 = 0, 0
    delta = 0.0001

    err = 0
    for i in range(20):
        a, b = A, B
        for i in range(10):
            u1 = (b + a - delta) / 2
            u2 = (b + a + delta) / 2
             
            if f(u1, y0) < f(u2, y0):
                b = u2
            else:
                a = u1
        x0 = (a + b) / 2
        err = abs(b - a)

        a, b = A, B
        for i in range(10):
            u1 = (b + a - delta) / 2
            u2 = (b + a + delta) / 2
             
            if f(x0, u1) < f(x0, u2):
                b = u2
            else:
                a = u1
        y0 = (a + b) / 2
        err = max(err, abs(b - a))

    return x0, y0, err

x0, y0, err= coord_descent()
print(x0, y0, err)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

X = np.arange(A, B, 0.001)
Y = np.arange(A, B, 0.001)
X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
Z = X**3 + 8 * Y**3 - 6 * X * Y + 1

surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
# ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
