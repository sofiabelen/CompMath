# import matplotlib.pyplot as plt
import numpy as np
# import seaborn as sns
from sympy import *
# from sympy import var, plot_implicit, symbols, Eq, And
from sympy.plotting import plot_parametric

def f1(x, y):
    return np.sin(x + 2) - y - 1.5

def f2(x, y):
    return np.cos(y - 2) + x - 0.5

def df1dx(x, y):
    return np.cos(x + 2)

def df1dy(x, y):
    return -1

def df2dx(x, y):
    return 1

def df2dy(x, y):
    return -np.sin(y - 2)

def newton():
    xcur = 0
    ycur = 0
    xnxt, ynxt = xcur, ycur

    for i in range(7):
        xcur, ycur = xnxt, ynxt
        denom = -np.cos(xcur + 2) * np.sin(ycur - 2) + 1

        f1cur = f1(xcur, ycur)
        f2cur = f2(xcur, ycur)

        xnxt = xcur - 1 / denom * ((-np.sin(ycur - 2)) * f1cur + (1) * f2cur)
        ynxt = ycur - 1 / denom * ((-1) * f1cur + (np.cos(xcur + 2)) * f2cur)
        err = max(abs(xcur - xnxt), abs(ycur - ynxt))
        print("Error: ", err)

    return xnxt, ynxt

x0, y0 = newton()
print("Intersection: ", x0, y0)

var('x y')
p1 = plot_implicit(Eq(sin(x + 2) - y - 1.5, 0), show=False)
p2 = plot_implicit(Eq(x + cos(y - 2) - 0.5, 0), show=False)
p4 = plot_implicit(Eq(x, x0), show=False)
p3 = plot_parametric((x, y0), (x, -5, 5), show=False)
p1.append(p2[0])
p1.append(p3[0])
p1.append(p4[0])
p1.show()
