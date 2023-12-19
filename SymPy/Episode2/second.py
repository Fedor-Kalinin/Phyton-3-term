import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

data = np.loadtxt('data.txt', skiprows=1)
N = data.shape[1]
A, B = np.array_split(data, [N], axis=0)
B = B.T


plt.bar(np.arange(N), (sp.linalg.solve(A, B)).T[0], color = "red")
plt.grid()

plt.savefig('result.png')

plt.show()