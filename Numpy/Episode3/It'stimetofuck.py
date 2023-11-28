import matplotlib.pyplot as plt
import numpy as np

import pandas as pd


import plotly
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots


data = np.array([])

with open('vek.csv', 'r') as f:
    data = np.append(data, f.read().split() )

data = data.astype(float)
A = np.eye(len(data))


for i in range(len(data)):
    A[i][i-1] = -1
# print(data.T)
b = A.dot(data)


datasave = np.full((len(data),255), 0)
datasave[:,0] = data

for i in range(1,255):
    datasave[:, i ]= datasave[:,(i-1)] - 0.5*(A.dot(datasave[:,(i-1)]))
    
print(data)
print(datasave[:,2])


# data = pd.DataFrame(datasave)

# df = px.data
# px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
#            size="pop", color="continent", hover_name="country",
#            log_x=True, size_max=55, range_x=[0,100], range_y=[0,100])
for i in range(25):
    plt.plot(datasave[:,i])
    a = str(i)
    plt.savefig(a)
    plt.close()
# plt.show()
# print(b)
# print('======')
# print(A)
