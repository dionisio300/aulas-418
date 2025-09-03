from classes import Carro, ContaBancaria

carro1 = Carro(14,'Preto','Celta','Chevrolet',2009,0)

# Acessar os Atributos
print(f'O modelo desse carro é {carro1.modelo}')
print(f'A velocidade atual é {carro1.v}')
print(f'O Ano do carro é {carro1.ano}')

# Executando métodos do objeto

print(carro1.acelerar(10))
print(carro1.acelerar(10))
print(carro1.acelerar(10))
print(carro1.acelerar(10))

print(f'A velocidade atual é {carro1.v}')

carro1.frear()
carro1.frear()
carro1.frear()

print(f'A velocidade atual é {carro1.v}')


'''
Aula10
|- poo.py
|- classes
    |- carro.py


'''

conta1 = ContaBancaria('João', 1000)
print(f'Saldo do {conta1.titular}')
conta1.mostrarSaldo()

conta1.__saldo = 20000

conta1.mostrarSaldo()

