import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def f1(x):
    if 20 <= x and x <= 28:
        return 1 + 20 / 8 - x / 8
    else:
        return 0

def f2(x):
    if 20 <= x and x <= 28:
        return -20 / 8 + x / 8
    elif 28 < x and x <= 39:
        return 1 + 28 / 11 - x / 11
    else:
        return 0

def f3(x):
    if 28 <= x and x <= 39:
        return - 28 / 11 + x / 11
    elif 39 < x and x <= 45:
        return 1 + 39 / 6 - x / 6
    else:
        return 0

def f4(x):
    if 39 <= x and x <= 45:
        return -39 / 6 + x / 6
    else:
        return 0

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

x = data['x']
y = data['y']

f = [f1, f2, f3, f4]
a = [491.94, 520.60, 825.68, 1419.50]

sns.set(context='notebook', style='darkgrid')
fig, ax = plt.subplots(figsize=(6, 6))

yf = np.zeros((4, len(x)))
ypred = np.zeros(len(x))
lab = ['$f1$', '$f_2$', '$f_3$', '$f_4$']
val = np.zeros(4)
loss = 0
for j in range(4):
    for i in range(len(x)):
        yf[j][i] = f[j](x[i])
        val[j] += yf[j][i] * y[i]
        ypred[i] += a[j] * f[j](x[i])

loss = np.sum((ypred[i] - y[i])**2)
print("Loss =", loss)

plt.scatter(x, y, label='Исходные данные')
plt.plot(x, ypred, label=r'$y(x) = a_1 \varphi_1(x) + a_2 \varphi_2(x) + a_3 \varphi_3(x) + a_3 \varphi_4(x)$')

ax.legend()
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')

fig.savefig("img/graph3.pdf")
plt.show()
