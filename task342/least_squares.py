import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.optimize import curve_fit
from scipy.interpolate import UnivariateSpline

def line(x, a, b):
    return a*x + b

data = np.genfromtxt('data.csv', names=True)
x = data['H']**(-1)
y = data['B']**(-1)

xiyi = np.sum(x * y)
xi2  = np.sum(x**2)
yi2  = np.sum(y**2)
xi   = np.sum(x)
yi   = np.sum(y)
# xiyi = 0
# xi2  = 0
# yi2  = 0
# xi   = 0
# yi   = 0
# 
# for i in range(len(x)):
#     xiyi += x[i] * y[i]
#     xi2  += x[i]**2
#     yi2  += y[i]**2
#     xi   += x[i]
#     yi   += y[i]

print(xiyi)
print(xi2)
print(yi2)
print(xi)
print(yi)

n = len(x) - 1
denom = ((n + 1) * xi2 - xi**2)
a = ((n + 1) * xiyi - xi * yi) / denom 
b = (yi * xi2 - xiyi * xi)     / denom
print("a =", a)
print("b =", b)

sns.set(context='notebook', style='darkgrid')
fig, ax = plt.subplots(figsize=(6, 6))

plt.plot(x, y)
plt.plot(x, a * x + b)

plt.show()
