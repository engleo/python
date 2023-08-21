from conta import Conta


def cadastrar_conta(numero, titular, saldo, limite):
    conta = Conta(numero, titular, saldo, limite)
    return conta

if(__name__ == "__main__"):
    cadastrar_conta()   
    