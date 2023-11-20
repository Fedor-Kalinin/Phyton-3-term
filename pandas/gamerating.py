import pandas as pd

g_name = input()
r_name = input()

rates = pd.read_csv(r_name, sep=";")
games = pd.read_csv(g_name, sep=";")

rates = rates.groupby('id').mean()

whole = pd.merge(games, rates, on='id')

best = whole.sort_values('mark', ascending=False).head(3)

for val in best.values:
    print(f'{val[1]} {val[-1]:.3f}')

dev = whole[whole['mark'] > 8].groupby('company').count().sort_values('id', ascending=False).head(1)

print(dev.index[0], dev.iloc[0, 0])
