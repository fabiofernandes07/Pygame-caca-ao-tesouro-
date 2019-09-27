import funçao
import pygame
import random
from matriz import matriz

#pontos
jogador1 = 0
jogador2 = 0
#cores da vez
c1 = 255
c2 = 0
jogadas = 1

#matriz aparência
matrizpy = [[' ']*4 for i in range(4)]

#iniciar
pygame.init()

pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()

#imagens
imagem_fundo = pygame.image.load("fundo.jpg")
imagem_fundo2 = pygame.image.load("fundo2.jpg")
imagem_buraco = pygame.image.load("buraco.png")
imagem_tesouro = pygame.image.load("tesouro.png")
imagem_zero = pygame.image.load("0.png")
imagem_um = pygame.image.load("1.png")
imagem_dois = pygame.image.load("2.png")
imagem_tres = pygame.image.load("3.png")
imagem_quatro = pygame.image.load("4.png")
vetimag = [imagem_zero,imagem_um,imagem_dois,imagem_tres,imagem_quatro]

#cores:
white = (255,255,255)
black = (0,0,0)
blue = (0,0,255)
red = (255,0,0)

#tela
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Caça ao Tesouro by Fábio e Dayvison")
screen.fill(white)

#fontes e textos
fonte = pygame.font.SysFont ("Comic Sams MS", 50)
joga1 = fonte.render("Jogador 1:",False,(255,0,0))
joga2 = fonte.render("Jogador 2:",False,(0,0,0))
pontos1 = fonte.render(str(jogador1),False,(0,0,0))
pontos2 = fonte.render(str(jogador2),False,(0,0,0))
ganhou = fonte.render("GANHOU",False,(255,0,0))
ninguem = fonte.render("NINGUEM",False,(255,0,0))

for i in range(0,200):
    screen.blit(imagem_fundo,(0,0))

    pygame.display.update()

#tela de inicio
screen.fill(white)
pygame.display.update()

#controle de tela e jogo
controle = True
while(controle):
    screen.blit(imagem_fundo2,(0,0))
    for evento in pygame.event.get():
        if(evento.type == pygame.QUIT):
            controle = False
        if(evento.type == pygame.MOUSEBUTTONUP):
            x , y = pygame.mouse.get_pos()
            if(x > 400 or y > 400):
                continue
            x = x//100
            y = y//100

            if (matrizpy[x][y] != " "):
                continue

            matrizpy[x][y] = matriz[x][y]

            #CONTROLE DE JOGADAS
            if(jogadas % 2 !=0):
                c1 = 0
                c2 = 255
                if (matriz[x][y] == "T"):
                    jogador1 = jogador1 + 100
                    pygame.mixer.music.load('acertou.mp3')
                    pygame.mixer.music.play()

                elif (matriz[x][y] == "B" and jogador1 > 0):
                    jogador1 = jogador1 - 50
                    pygame.mixer.music.load('errou.mp3')
                    pygame.mixer.music.play()

                elif(matriz[x][y] == "B" ):
                    pygame.mixer.music.load('errou.mp3')
                    pygame.mixer.music.play()

            elif(jogadas % 2 ==0):
                c1 = 255
                c2 = 0
                if(matriz[x][y] == "T"):
                    jogador2 = jogador2 + 100
                    pygame.mixer.music.load('acertou.mp3')
                    pygame.mixer.music.play()

                elif(matriz[x][y] == "B" and jogador2 > 0):
                    jogador2 = jogador2 - 50
                    pygame.mixer.music.load('errou.mp3')
                    pygame.mixer.music.play()

                elif(matriz[x][y] == "B" ):
                    pygame.mixer.music.load('errou.mp3')
                    pygame.mixer.music.play()

            jogadas = jogadas + 1
            pygame.display.update()
        #produção na tela
        for i in range(4):
            for j in range(4):

                if (matrizpy[i][j] == ' '):
                    pygame.draw.rect(screen,(0,0,0),(i*100,j*100,100,100),1)
                elif(matrizpy[i][j] == "T"):
                    screen.blit(imagem_tesouro,(i*100,j*100))
                elif(matrizpy[i][j] == "B"):
                    screen.blit(imagem_buraco,(i*100,j*100))
                else:
                    screen.blit(vetimag[matrizpy[i][j]],(i*100,j*100))
            joga1 = fonte.render("Jogador 1:",False,(c1,0,0))
            joga2 = fonte.render("Jogador 2:",False,(c2,0,0))
            pontos1 = fonte.render(str(jogador1),False,(c1,0,0))
            pontos2 = fonte.render(str(jogador2),False,(c2,0,0))

            screen.blit(joga1,(400,20))
            screen.blit(joga2,(400,80))
            screen.blit(pontos1,(580,20))
            screen.blit(pontos2,(580,80))
            if(jogadas >= 17):
                screen.blit(ganhou,(580,170))
                if(jogador1 > jogador2):
                    screen.blit(joga1,(400,170))
                elif(jogador2 > jogador1):
                    screen.blit(joga2,(400,170))
                elif(jogador1 == jogador2):
                    screen.blit(ninguem,(400,170))

        pygame.display.update()
pygame.quit()
