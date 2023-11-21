import matplotlib.pyplot as plt
import numpy as np

data_prep = {}
data_group = {}

data = []
#reading data
with open('students.csv', 'r') as f:
    data = [j.split(';') for j in [i for i in f.readlines()]]
#distibuting data for preps and groups
for i in data:
    prep = i[0]
    group = i[1]
    mark = int(i[2])
    # For preps
    if(not(prep in data_prep.keys())):
        data_prep[prep] = [0]*10
    
    data_prep[prep][mark - 1] += 1

    # For groups
    if(not(group in data_group.keys())):
        data_group[group] = [0]*10

    data_group[group][mark - 1] += 1


fig, axs = plt.subplots(nrows=2,  figsize=(20,20))
fig.set_dpi(300)
axs = axs.flatten()

preps = list(data_prep.keys())
groups = list(data_group.keys())


new_data_prep = {'1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': [], '10': [],}

for i in preps:
    for j in range(1, 11):
        key = str(j)
        new_data_prep[key].append(data_prep[i][j - 1]) 

#this needs for stacking bars on top of each other
#making our bar graph for preps
bottom = np.zeros(len(preps))
for i in range(1, 11):
    key = str(i)
    p = axs[0].bar(preps, new_data_prep[key], label=key, bottom=bottom)
    bottom += new_data_prep[key]
axs[0].set_title('Marks per prep')


#same for groups

#making dictionary for groups
new_data_group = {}
for i in range(1, 11):
    key = str(i)
    new_data_group[key] = []

#filling it
for i in groups: 
    for j in range(1, 11):
        key = str(j)
        new_data_group[key].append(data_group[i][j - 1]) 

#making our bar graph for groups
bottom = np.zeros(len(groups))
for i in range(1, 11):
    key = str(i)
    p = axs[1].bar(groups, new_data_group[key], label=key, bottom=bottom)
    bottom += new_data_group[key]
axs[1].set_title('Marks per group')

axs[0].legend(loc=1)
axs[1].legend(loc=1)
plt.savefig('G.png')
plt.show()