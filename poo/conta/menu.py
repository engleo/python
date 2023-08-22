from conta import Conta
from cadastrar_conta import cadastrar_conta

def iniciar(): 
    resposta = int(input("Cadastrar nova conta( 1 - Sim / 2 - Não ): "))
    return resposta

resposta = iniciar()
numero = 1
while (resposta == 1):
    titular = input("Digite o nome do titular: ")
    saldo = int(input("Digite o saldo inicial: "))
    limite = 1000 
    
    cadastrar_conta(numero, titular, saldo, limite)


    