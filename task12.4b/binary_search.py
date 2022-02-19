import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def f(x):
    return np.arctan(x - 1) + 2 * x

def binary_search():
    a = 0.2
    b = 0.4
    for i in range(11):
        c = (a + b) / 2
        # print(a, b)
        if f(c) < 0:
            a = c
        else:
            b = c
    print("error ", b - a)
    return (a + b) / 2

root = binary_search()
print("Root: ", root)

sns.set(context='notebook', style='darkgrid')
fig, ax = plt.subplots(figsize=(6, 6))

ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')

plt.axvline(x=root, color='pink', label="Root")

x = np.arange(-5, 5, 0.001)
ax.plot(x, -2 * x, '--', label=r"$-2x$")
ax.plot(x, np.arctan(x - 1), '--',  label=r"$\arctan(x - 1)$")
ax.legend()

fig.savefig("img/graph1.pdf")
plt.show()
