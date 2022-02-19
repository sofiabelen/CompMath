import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def f(x):
    return x**2

x = np.linspace(0, 1, 50)
y = f(x)

xiyi = np.sum(x * y)
xi2  = np.sum(x**2)
yi2  = np.sum(y**2)
xi   = np.sum(x)
yi   = np.sum(y)

n = len(x)
denom = (n * xi2 - xi**2)
a = (n * xiyi - xi * yi) / denom 
b = (yi * xi2 - xiyi * xi)     / denom

sns.set(context='notebook', style='darkgrid')
fig, ax = plt.subplots(figsize=(6, 6))

plt.scatter(x, y, label='$f(x) = x^2$')
plt.plot(x, x * a + b,
        label=rf'$f(x) = xa + b, a = {a:.2f}, b = {b:.2f}$', c='r')

ax.legend()
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')

fig.savefig("img/graph1.pdf")
plt.show()
