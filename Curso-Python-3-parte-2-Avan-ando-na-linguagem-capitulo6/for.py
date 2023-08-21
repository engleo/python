import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!\nEscolha um numero de 1 a 50")
print("*********************************")
nivel = int(input("Escolha o nível:\n1 - Fácil\n2 - Médio\n3 - Dificil\n"))

numero_secreto = int(random.randrange(1,50))
if(nivel == 1):
    total_de_tentativas = 10
elif(nivel == 2):
    total_de_tentativas = 7
else:
    total_de_tentativas = 3        


for rodada in range(1,total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    chute_str = input("Digite o seu número: ")
    print("Você digitou " , chute_str)
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
        elif(menor):
            print("O seu chute foi menor do que o número secreto!")

    
if rodada >= 3 and not(acertou):
    print("Acabaram as tentativas e o número é o: ", numero_secreto)
print("Fim do jogo")