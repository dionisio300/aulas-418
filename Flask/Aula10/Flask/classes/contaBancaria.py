class ContaBancaria:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo
    def sacar(self,valor):
        if self.saldo < valor:
            return f'Não foi possível sacar'
        else:
            self.saldo -= valor
            return self.saldo
    def depositar(self,valor):
        self.saldo += valor
        return self.saldo