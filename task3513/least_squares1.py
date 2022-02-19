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
    
    print(xi)
    print(yi)
    print(xi2)
    print(yi2)
    print(xiyi)
    n = len(x)
    denom = (n * xi2 - xi**2)
    a = (n * xiyi - xi * yi) / denom 
    b = (yi * xi2 - xiyi * xi)     / denom
    print("a = ", a, "b = ", b)
    return a, b

data = np.genfromtxt('data.csv', names=True)

x = data['x']
y = data['y']
a, b = lsm(x, y)

loss = np.sum((y - a * x - b)**2)
print("Loss1 =", loss)

sns.set(context='notebook', style='darkgrid')
fig, ax = plt.subplots(figsize=(6, 6))

plt.scatter(x, y, label='Исходные данные')
plt.plot(x, x * a + b,
        label=rf'$f(x) = xa + b, a = {a:.2f}, b = {b:.2f}$')

ax.legend()
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')

fig.savefig("img/graph1.pdf")
plt.show()
