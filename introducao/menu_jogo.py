import adivinhacao
import forca

print("*********************************")
jogo = int(input("Bem vindo ao menu do Jogo!\nEscolha o jogo\n1 - Adivinhacao\n2 - Forca\n"))

if(jogo == 1):
    adivinhacao.jogar()
else:
    forca.jogar()    