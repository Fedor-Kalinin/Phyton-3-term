import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from numpy import fft
name = 'signal03.dat'
data = []
with open (name, 'r') as f:
    data = [float(line.strip()) for line in f]

# data1 = []
#Как указать функции что я передаю массив определенныз данных 
# def revers ( da : float, i, k ): 
#     sum = 0.
#     if i != 0 and k != 10 and type(da[i]) == float:
#         k += 1
#         sum = float(da[i]) + revers(da, (i-k), k )
#     else:
#         return sum


# data = np.cumsum(data)

# d = np.array([50, 55, 36, 49, 84, 75, 101, 86, 80, 104, 12, 1])


# print(d)


def moving_average(arr):
    result = [arr[0]]
    for i in range(1, len(arr)):
        if i < 10:
            result.append(sum(arr[:i+1]) / (i+1))
        else:
            result.append(sum(arr[i-9:i+1]) / 10)
    return result

# window_size = d.shape[0] // 70
# denoised_data: np.ndarray = (
# 	pd.Series(d[:])
# 	.rolling(window=window_size)
# 	.mean()
# 	.iloc[window_size - 1 :]
# 	.values
# )
# print(denoised_data)
# plt.plot(d)
# plt.plot(denoised_data)


print( moving_average(data))
# plt.scatter( data1, data)
plt.plot(moving_average(data))
plt.plot(data) 
plt.savefig("NOnoise3.png")
plt.show()
# print(data)
