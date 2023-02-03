class Conta:

    def __init__(self, numero, titular, saldo, limite ):
        print("construindo um objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor
        print("valor do deposito foi de {}".format(valor))

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
            print("valor do saque foi de {}".format(valor))
        else:
            print("o valor {} passou de seu limite".format(valor))


    def transferir(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
        print("o valor {} foi trasnferido para {}".format(valor,destino))

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
    def limite(self,limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigod_bancos():
        return {'BB':'001','caixa':'104','Bradesco':'237'}