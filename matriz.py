from random import randint


#buracos
cont6 = 0
#tesouros
cont5 = 0
#nada
cont4 = 0
lista=["T","B",0]

matriz = []
for i in range(0,4):
    linhas = []
    for j in range(0,4):
        linhas.append(lista[randint(0,2)])
    matriz.append(linhas)

#buracos
for i in range(4):
    for j in range(0,4):
        if (matriz[i][j] == lista[1] ):
            cont6 += 1
        if (matriz[i][j] == lista[1] and cont6 == 4):
            matriz[i][j] = lista[2]
            cont6 -= 1
#vazio
for i in range(0,4):
    for j in range(0,4):
        if(matriz[i][j] == lista[2]):
            cont4 += 1
        if(cont4 > 7):
            matriz[i][j] = lista[0]
            cont4 -= 1



#tesouro
for i in range(0,4):
    for j in range(0,4):
        if (matriz[i][j] == lista[0] ):
            cont5 += 1
        if (cont5 > 6 ):
            matriz[i][j] = lista[2]
            cont5 -= 1
