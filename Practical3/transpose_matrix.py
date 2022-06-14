# Apoorv Varkute
# Transpose of Matrix 

a=[[12,7],
    [4,5],
    [3,8]]

r= [[0,0,0],
    [0,0,0]]

for i in range(len(a)):
    for j in range(len(a[0])):
        r[j][i] = a[i][j]

for i in r:
    print(i)