class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} da conta {}, do titular {}".format(self.__saldo, self.__numero, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        if (self.__saldo >= valor):
            self.__saldo -= valor
        else:
            print("Sem limite!")    

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def limite(self):
        return self.__limite        

    @property
    def titular(self):
        return self.__titular

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    @titular.setter
    def titular(self, titular):
        self.__titular = titular    





    