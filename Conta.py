class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("O titular {} possui um saldo de {}".format(self.__titular, self.__saldo))

    def deposito(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor):
        disponivel = self.__saldo + self.__limite
        return valor <= disponivel

    def saca(self, valor):
        if not self.__pode_sacar(valor):
            print("Valor muito alto! Seu limite é de apenas {} reais".format(self.__limite))
        else:
            self.__saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposito(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    # static methods do not require to create an object previously
    @staticmethod
    def codigo_banco():
        return "001"
