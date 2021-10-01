import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

x = np.arange(1.92, 2.08, 10e-4)
p = np.zeros(len(x))
a = [1, -18, 144, -672, 2016, -4032, 5376, -4608, 2304, -512]

for i in range(len(x)):
    for j in range(len(a)):
        p[i] = x[i] * p[i] + a[j]

sns.set(context='notebook', style='darkgrid')
fig, ax = plt.subplots(figsize=(6, 6))

ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')

plt.plot(x, p, label='Метод Горнера')
plt.plot(x, (x - 2)**9, label=r'$y = (x - 2)^9$')

ax.legend()

fig.savefig("img/graph1.pdf")
plt.show()
