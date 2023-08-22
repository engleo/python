from conta import Conta
from cadastrar_conta import cadastrar_conta

def iniciar_cadastrar(): 
    resposta = int(input("Cadastrar nova conta( 1 - Sim / 2 - Não ): "))
    return resposta

def acessar_conta():
    resposta_acessar = int(input("Digite o numero da conta: "))
    return resposta_acessar

resposta = iniciar_cadastrar()
numero = 1
contas = {}
while (resposta == 1):
    titular = input("Digite o nome do titular: ")
    saldo = int(input("Digite o saldo inicial: "))
    limite = 1000 
    
    conta = cadastrar_conta(numero, titular, saldo, limite)
    contas[numero] = conta
    numero += 1
    resposta = iniciar_cadastrar()


while (resposta)
    