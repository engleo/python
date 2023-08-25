import db
from conta import Conta
from cadastrar_conta import cadastrar_conta


def iniciar_cadastrar(): 
    resposta = int(input("Cadastrar nova conta( 1 - Sim / 2 - Não ): "))
    return resposta

def acessar_conta():
    resposta_acessar = int(input("Digite o numero da conta: "))
    return resposta_acessar


def main():
    resposta = iniciar_cadastrar()
    numero = 1
    
    while (resposta == 1):
        titular = input("Digite o nome do titular: ")
        saldo = int(input("Digite o saldo inicial: "))
        limite = int(input("Digite o limite inicial: "))
        cadastrar_conta(numero, titular.title(), saldo, limite)
        db.set_conta(titular.title(), saldo, limite)
        numero += 1
        resposta = iniciar_cadastrar()

    

if __name__ == "__main__":
    db.criar_tabela_conta()
    main()
    rows = db.get_all_conta()
    for row in rows:
        print (row)
    
    
    