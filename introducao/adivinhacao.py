import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!\n")
    print("*********************************")
    nivel = int(input("Escolha o nível:\n1 - Fácil\n2 - Médio\n3 - Dificil\n"))

    numero_secreto = int(random.randrange(1,50))
    if(nivel == 1):
        total_de_tentativas = 10
    elif(nivel == 2):
        total_de_tentativas = 7
    else:
        total_de_tentativas = 3        

    menor_numero = 1
    maior_numero = 50

    for rodada in range(1,total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Escolha um numero de {} a {}\n".format(menor_numero, maior_numero))
        print("Você digitou:" , chute_str)
        chute = int(chute_str)

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Parabéns, você acertou!")
            break;
        else:
            if(maior):
                print("O seu chute foi maior do que o número secreto!")
                maior_numero = chute
            elif(menor):
                print("O seu chute foi menor do que o número secreto!")
                menor_numero = chute

        
    if rodada >= 3 and not(acertou):
        print("Acabaram as tentativas e o número é o:", numero_secreto)
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()