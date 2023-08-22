from conta import Conta


def cadastrar_conta(numero, titular, saldo, limite):
    conta = Conta(numero, titular, saldo, limite)
    return conta

cadastrar_conta(10, "leo", 5000, 100000)