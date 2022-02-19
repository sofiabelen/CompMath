import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def f(x):
    return x**2

def lsm(x, y):
    xiyi = np.sum(x * y)
    xi2  = np.sum(x**2)
    yi2  = np.sum(y**2)
    xi   = np.sum(x)
    yi   = np.sum(y)
    
    n = len(x)
    denom = (n * xi2 - xi**2)
    a = (n * xiyi - xi * yi) / denom 
    b = (yi * xi2 - xiyi * xi)     / denom
    return a, b

data = np.genfromtxt('data.csv', names=True)

x1 = data['x'][0:9]
y1 = data['y'][0:9]
x2 = data['x'][8:20]
y2 = data['y'][8:20]
x3 = data['x'][19:]
y3 = data['y'][19:]
print(x1)
print(x2)
print(x3)
# x = data['x']
# y = data['y']
# a, b = lsm(x, y)

x = [x1, x2, x3]
y = [y1, y2, y3]
a = []
b = []

for i in range(3):
    ai, bi = lsm(x[i], y[i])
    a.append(ai)
    b.append(bi)

Loss = np.sum((y1 - a[0] * x1 - b[0])**2) + np.sum((y2 - a[1] * x2 - b[1])**2) + np.sum((y3 - a[2] * x3 - b[2])**2)
print("Loss2 = ", Loss)

sns.set(context='notebook', style='darkgrid')
fig, ax = plt.subplots(figsize=(6, 6))

lab = ['[20, 28]', '[28, 39]', '[39, 45]']

for i in range(3):
    plt.scatter(x[i], y[i], label=lab[i])
    plt.plot(x[i], x[i] * a[i] + b[i],
            label=rf'$f(x) = xa + b, a = {a[i]:.2f}, b = {b[i]:.2f}$')

ax.legend()
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')

fig.savefig("img/graph2.pdf")
plt.show()
