import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def f(t):
    return (t - 5) * np.exp(t)

def binary_search():
    a = -3
    b = 5
    delta = 0.0001
    for i in range(20):
        u1 = (b + a - delta) / 2
        u2 = (b + a + delta) / 2
         
        if f(u1) < f(u2):
            b = u2
        else:
            a = u1

    return (b + a) / 2, b - a

x, err = binary_search()
print("x_min = ", x, " err: ", err)

sns.set(context='notebook', style='darkgrid')
fig, ax = plt.subplots(figsize=(6, 6))

ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')

x = np.arange(-3, 5, 0.00001)
ax.plot(x, f(x), label=r"$(x - 5) e^x$")

ax.legend()

fig.savefig("img/graph1.pdf")
plt.show()
