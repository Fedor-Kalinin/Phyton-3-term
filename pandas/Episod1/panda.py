
import pandas as pd
import numpy as np

dan = "./transactions.csv"
coll = ['0', 'CONTRACTOR', 'STATUS' , 'SUM']
# data = []
# with open (dan, 'r') as f:
#     data = f.readlines()
df = pd.read_csv(dan, header=None,  sep=',')
# data.pop(0)
# data1 = []
# for i in range(len(data)):
#     n, firstname, secondname, status, sum = data[i].split(',')
#     data[i] = (firstname + ',' + secondname).replace('"', ''), status, int(sum.replace('\n', ''))
# # df = pd.DataFrame(data, columns = coll)
# df[df['STATUS'] == 'OK']
# target = df.loc[df['STATUS'] == 'OK'].sort_values(by='SUM', ascending=False)
# # df.columns = ['CONTRACTOR', 'STATUS' , 'SUM']
# print(target)


df.columns=coll
# del df['0']
df.drop(labels = [0],axis = 0, inplace = True)
df.drop(columns=['0'], inplace=True)
df = df.reset_index(drop=True)
# df.columns = ['CONTRACTOR', 'STATUS' , 'SUM']
df['SUM'] = df['SUM'].astype(int)

target = df.loc[df['STATUS'] == 'OK'].sort_values(by='SUM', ascending=False)
print(target[:3])

print( target.loc[df['CONTRACTOR'] == 'Umbrella, Inc'].groupby(by = 'CONTRACTOR').sum()['SUM'])



# print(target[:4])

# print('========')
# print(df)
