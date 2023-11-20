import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

dan = "./flights.csv"
coll = ['0', 'CARGO', 'PRICE' , 'WEIGHT']

df = pd.read_csv(dan, header=None,  sep=',')

df.columns=coll

df.drop(labels = [0],axis = 0, inplace = True)
df.drop(columns=['0'], inplace=True)
df = df.reset_index(drop=True)

df['WEIGHT'] = df['WEIGHT'].astype(int)
df['PRICE'] = df['PRICE'].astype(int)

datanameco = df["CARGO"].unique()

count = []

price = []

weight = []

priseonepartofweight = []

for i in range(len(datanameco)):

    count.append(len(df.loc[df['CARGO']==datanameco[i]]))
    print("Назвавние компании и колличество рейсов",datanameco[i], count[i] )

    weight.append(df.loc[df['CARGO']==datanameco[i]].sum()['WEIGHT'])
    print("Назвавние компании и суммарный вес ",datanameco[i], weight[i])

    price.append( df.loc[df['CARGO']==datanameco[i]].sum()['PRICE'] )
    print("Назвавние компании и заработанное бабло ",datanameco[i], price[i])

for i in range(len(datanameco)):
    priseonepartofweight.append(price[i]/weight[i])


fig = plt.figure(figsize=(20,10))

ax1 = fig.add_subplot(141)
ax1.bar(datanameco, count)
ax1.set_title("Колличество полетов")

ax2 = fig.add_subplot(142)
ax2.bar(datanameco, price)
ax2.set_title("Заработаное бабло")

ax3 = fig.add_subplot(143)
ax3.bar(datanameco, weight)
ax3.set_title("Суммарный перевезенный вес")

ax4 = fig.add_subplot(144)
ax4.bar(datanameco,priseonepartofweight)
ax4.set_title("Цена единицы веса")
plt.subplots_adjust(wspace=0.7, hspace=0.4)
plt.savefig("Gista.png")

plt.show()
print (datanameco)

# print(df)