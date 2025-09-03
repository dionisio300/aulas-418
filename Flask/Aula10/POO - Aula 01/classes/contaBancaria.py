class ContaBancaria:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.__saldo = saldo
    def sacar(self,valor):
        if self.__saldo < valor:
            return f'Não foi possível sacar'
        else:
            self.__saldo -= valor
            return self.__saldo
    def depositar(self,valor):
        self.__saldo += valor
        return self.__saldo
    
    def mostrarSaldo(self):
        print(f'O saldo da conta é {self.__saldo}')