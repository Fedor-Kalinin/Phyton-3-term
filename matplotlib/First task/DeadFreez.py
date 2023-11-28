import matplotlib.pyplot as plt
import numpy as np
import math 
array = []

x=[]
y=[]
with open('/Users/Фёдор/Downloads/dead_moroz/005.dat', 'r') as a:
    array = a.read().split()
 
for i in range(1, (int(array[0])*2+1)):
    if i%2 != 0 :
        x.append(float(array[i]))
    if i%2 == 0 :
        y.append(float(array[i]))

r=[]
theta=[]
for i in range(int(array[0])):
    c = math.sqrt(x[i]**2 + y[i]**2)
    if y[i] >=0:
        r.append(c)
        theta.append(math.acos(x[i]/c))
    else:
        r.append(c)
        theta.append(-math.acos(x[i]/c))


fig = plt.figure(figsize=(20,10))


ax1 = fig.add_subplot(122, projection='polar')
ax1.scatter(theta, r, marker='.', color='red')
ax1.set_rmax(max(r)*1.08)
g= int(max(r)/5)
ax1.set_rticks([g, 2*g, 3*g, 4*g, 5*g]) 

ax1.set_title("Fire in polar")

#соотношения сторон
kwargs ={'aspect' : '1' }

ax2 = fig.add_subplot(121, **kwargs )
ax2.scatter(x, y, marker='.', color='red')

ax2.set_title("Fire in classic")

ax2.set_xlabel('X')
ax2.set_ylabel('Y')

plt.figure(dpi=300)

plt.savefig("005.png")
plt.show()





