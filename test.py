import numpy as np
import matplotlib.pyplot as plt

n = 10000
N = np.random.normal(10, 0.2, n)
t = np.linspace(0, n, n)

plt.hist(N, bins = 44)
plt.show()