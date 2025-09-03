class Veiculo:
    def __init__(self,marca, modelo, ano, preco):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco = preco
    def exibirInformacoes(self):
        informacoes = f'Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}\nPreço: {self.preco}'

        return informacoes
class Carro(Veiculo):
    def __init__(self,marca, modelo, ano, preco,nPortas,tipoCombustivel):
        super().__init__(marca, modelo, ano, preco)
        self.nPortas = nPortas
        self.tipoCombustivel = tipoCombustivel
    def dirigir(self):
        return f'Dirigindo!!'


