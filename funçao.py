from matriz import matriz




for i in range(4):
    for j in range(4):
        cont0 = 0



        if(matriz[i][j] == 0):
                if i + 1 <= 3:
                    if(matriz[i + 1][j] == "T"):
                        cont0 += 1

                if i - 1 >= 0:
                    if(matriz[i - 1][j] == "T"):
                        cont0 += 1

                if j + 1 <= 3:
                    if(matriz[i][j + 1] == "T"):
                        cont0 += 1

                if j - 1 >= 0:
                    if(matriz[i][j - 1] == "T"):
                        cont0 += 1



                matriz[i][j] = cont0
