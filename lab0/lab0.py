import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

a = 0
b = 1
E = 2**(-53)
M4 = 1
h_opt1 = (8 * E / M4)**(1 / 3)
h_opt2 = (48 * E / M4)**(1 / 4)

def f(x):
    return x + np.cos(x)

def f_2der(x):
    return -np.cos(x)

def f_2der_1por(h):
    n = int((b - a) / h)
    ans = np.zeros(n)
    sigma = 0

    for i in range(n):
        x0 = a + (i - 2) * h
        x1 = a + (i - 1) * h
        x2 = a + i       * h
        ans[i] = (f(x0) - 2 * f(x1) + f(x2)) / h**2
        sigma += (ans[i] - f_2der(a + i * h))**2

    sigma = (sigma / n)**(1 / 2)
    return ans, sigma

def f_2der_2por(h):
    n = int((b - a) / h)
    ans = np.zeros(n)
    sigma = 0

    for i in range(n):
        x0 = a + (i - 1) * h
        x1 = a + i       * h
        x2 = a + (i + 1) * h
        ans[i] = (f(x0) - 2 * f(x1) + f(x2)) / h**2
        sigma += (ans[i] - f_2der(a + i * h))**2

    sigma = (sigma / n)**(1 / 2)
    return ans, sigma

hs = np.arange(h_opt1 / 10, h_opt1 * 5, h_opt1 / 10)
sigmas = np.zeros(len(hs))
print(len(hs))
print(h_opt1, hs[9])

for i in range(len(hs)):
    print(i)
    ans, sigmas[i] = f_2der_1por(hs[i])

sns.set(context='notebook', style='darkgrid')
fig, ax = plt.subplots(figsize=(8, 8))

ax.set_xlabel(r'$h$')
ax.set_ylabel(r'$\sigma$')

plt.plot(hs, sigmas, label=r'$\sigma(h)$')
plt.scatter(h_opt1, sigmas[9], label=r'$h_{opt}$', c='g')

ax.legend()

fig.savefig("img/graph1.pdf")
fig.savefig("img/graph1.png")
plt.show()
