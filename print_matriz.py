from matriz import matriz
import funçao
import jogadores

controle = 0
jogador1 = 0
jogador2 = 0
jogadas = 1

matrizz = []
for i in range(0,4):
    linhas = []
    for j in range(0,4):
        linhas.append("#")
    matrizz.append(linhas)


def print_matriz():
    print("  1  2  3  4")

    for i in range(0,4):
        print(" ")
        print(i+1, end = "")

        for j in range(0,4):

            print("|",matrizz[i][j],end = "")
        print("|", end ="")


#jogo
while(controle == 0):
    print_matriz()
    print("\n")
    jogadores.vez()
    coluna = int(input("Digite a coluna: "))
    linha = int(input("Digite a linha: "))
    if coluna>4 or linha>4 :
        print("Número invaido")
        print(" ")
        coluna = int(input("Digite a coluna: "))
        linha = int(input("Digite a linha: "))
    matrizz[linha-1][coluna-1] = matriz[linha-1][coluna-1]
    jogadores.jogada()
    if(matrizz== matriz):
        if(jogadores.jogador1 > jogadores.jogador2):
            print("Jogador 1 ganhou")
        elif(jogadores.jogador2 > jogador1):
            print("Jogador 2 ganhou")
        print("\n*******FIM*******")
        controle = int(input("\nDigite 1 para sair"))
