'''
Crie uma classe para representar um produto.
Atributos:
- Nome (público)
- Preço (Privado)
- Descrição (Privado)
- Imagem (Privado)

Métodos:
- Mostrar o preço
- Modificr o preço
- Dar desconto de um valor que o usuário vai fornecer
- Aumentar o valor em x%
- Mostrar a descrição do produto
- Trocar a descrição
'''

from classes import Produto, Veiculo, Carro

imagem = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQDHJFA2oQXZeEaVA1wFTXpkgSltzPR6S5XLQ&s'

carro = Produto('Dolphin',100000,'Carro elétrico',imagem)

print(f'O preço é {carro.getPreco()}')
carro.setPreco(120000)
print(f'O preço é {carro.getPreco()}')
print(carro.setPreco(-120000))

carro.darDesconto(51)
print(f'O preço é {carro.getPreco()}')

'''
Crie uma classe chamada ReservaHotel com os seguintes requisitos:
1. Atributos privados:
__hospede (string)

__quarto (inteiro)

__diarias (inteiro)

2. Métodos públicos:

get_hospede() e set_hospede(nome) → só aceita string não vazia.

get_quarto() e set_quarto(numero) → só aceita número inteiro positivo.

get_diarias() e set_diarias(qtd) → só aceita inteiro maior que zero.

calcular_total(valor_diaria) → retorna o custo total da reserva.
'''

veiculo1 = Veiculo('BYD','Dolphin','2025','120000')
carro1 = Carro('BYD','Dolphin','2025','120000',4,'Eletricidade')
print(veiculo1.exibirInformacoes())