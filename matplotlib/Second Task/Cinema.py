import matplotlib.pyplot as plt
import numpy as np
import math
with open('data.txt', 'r') as f:
    data = [i.replace('\n','') for i in f.readlines()]
#Для полярных + , subplot_kw={'projection': 'polar'}
fig,  axs = plt.subplots(int((len(data)/4)), 2, figsize = (15,15))
axs = axs.flatten()
mx = 0
my = 0
Mx = 0
My = 0
# r=[]
# theta=[]
for i in range(int(len(data)/2)):
    x = [float(k) for k in data[2*i].split()]
    y = [float(k) for k in data[2*i+1].split()]
    
    # for b in range(int(len(data)/2)):
    #     c = math.sqrt(x[b]**2 + y[b]**2)
    # if y[b] >0:
    #     r.append(c)
    #     theta.append(math.acos(x[b]/c))
    # if y[b] == 0 and x[b] == 0:
    #     r.append(0)
    #     theta.append(0)
    # else:
    #     r.append(c)
    #     theta.append(-math.acos(x[b]/c))
    # r.clear
    # theta.clear
    if mx > min(x):
        mx = min(x)
    if Mx < max(x):
        Mx = max(x)
    if my > min(y):
        my = min(y)
    if My < max(y):
        My = max(y)
    Kadr = 'Kadr' + str(i)
    axs[i].plot(x,y)
    #axs[i].scatter(theta,r,marker='.', color='red')
    axs[i].set_title(Kadr)

for i in axs:
    i.set_xlim(mx, Mx)
    i.set_ylim(my, My)
    i.set_xticks(np.arange(mx, Mx, step=1))
    i.set_yticks(np.arange(-10.5, 12.5, step=1.5))
    i.grid(True)
    #polar
    # i.set_rmax(2.5)
    # g= 1
    # i.set_rticks([g, 2*g, 2.5]) 

#

plt.savefig("2.png")
plt.show()
