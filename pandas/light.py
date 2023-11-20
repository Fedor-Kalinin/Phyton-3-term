import numpy as np
N, M = list(int, input().split())
K = int(input())

field =  np.zeros((N, M), dtype = bool )

S =[]
for i in range(K):
    S.append(list(map(int, input().split())))
for lamp in S:
    X, Y, D  = lamp[0], lamp[1], lamp[2]
    field[max(0, X-D):min(M, X+D), max(0, Y-D):min(N, Y+D)] = True
print(fiel.)