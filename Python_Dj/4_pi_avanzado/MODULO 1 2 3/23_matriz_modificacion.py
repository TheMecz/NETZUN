pbi = [[2.9, 2.5], [3.9, 4.0], [0.9, 2.2], [1.5, 3.3],
       [1.8, 2.6], [1.0, 2.0], [2.2, 2.3], [4.0, 4.0],
       [2.5, 3.5], [3.0, 3.0], [-9.5, -8.5]]

row = 11
colum = 2

def recorrer_matriz():
    for i in range(row):
        for j in range(colum):
            print(pbi[i][j], end=" ")
        print()

print("ANTES")
recorrer_matriz()
pbi[2][1] = 999
print("DESPUES")
recorrer_matriz()