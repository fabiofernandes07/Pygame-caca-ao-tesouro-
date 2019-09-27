import print_matriz

jogador1 = 0
jogador2 = 0
jogadas = 1

def vez():
    global jogadas

    if (jogadas % 2 != 0):
        print("Jogador 1:")

    elif(jogadas % 2 == 0):
        print("Jogador 2:")

def jogada():
    global jogadas
    global jogador1
    global jogador2
    print(" ")
    if (jogadas % 2 != 0):

        if ( print_matriz.matrizz[ print_matriz.linha-1][ print_matriz.coluna-1] == "T"):

            jogador1 += 100

            print("BOA MARUJO!!")
            print("\nJogador 1 ganhou  100 pontos e está com o saldo de %d pontos"%jogador1)

        elif ( print_matriz.matrizz[ print_matriz.linha-1][ print_matriz.coluna-1] == "B" and jogador1 > 0 ):
            jogador1 -= 50

            print("EROOOU!!")
            print("\nJogador 1 perdeu 50 pontos e está com o saldo de %d pontos."%jogador1)

        else:
            print("Tente novamente na sua próxima jogada marujo!!")

    elif(jogadas % 2 == 0):
        if ( print_matriz.matrizz[ print_matriz.linha-1][ print_matriz.coluna-1] == "T"):
            jogador2 += 100

            print("BOA MARUJO!!")
            print("\nJogador 2 ganhou  100 pontos e está com o saldo de %d pontos."%jogador2)

        elif ( print_matriz.matrizz[ print_matriz.linha-1][ print_matriz.coluna-1] == "B" and jogador2 > 0 ):
            jogador2 -= 50

            print("EROOOU")
            print("\nJogador 2 perdeu 50 pontos e está com o saldo de %d pontos."%jogador2)

        else:
            print("Tente novamente na sua próxima jogada marujo!!")
    jogadas = jogadas + 1
    print(" ")
