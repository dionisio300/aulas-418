class Produto:
    # Atributos na função construtora
    def __init__(self,nome,preco,descricao,imagem):
        self.nome = nome
        self.__preco = preco
        self.__descricao = descricao
        self.__imagem = imagem
    # Métodos 
    def getPreco(self):
        return self.__preco
    def setPreco(self,novoPreco):
        if novoPreco >= 0:
            self.__preco = novoPreco
            return 'Preço Atualizado'
        else:
            return 'Erro'
    def darDesconto(self,desconto):
        if desconto > 50:
            return 'Não é possivel dar esse desconto'
        elif desconto < 0:
            return 'Valor inválido'
        else:
            valorDesconto = self.__preco * desconto/100
            self.__preco -= valorDesconto
            return f'Desconto de {desconto}% foi aplicado com sucesso'
    def aumentarValor(self,aumento):
        if aumento > 0:
            valorAumento = self.__preco * aumento/100
            self.__preco += valorAumento
            return f'Aumento de {aumento}% foi aplicado com sucesso'
        else: 
            return 'Valor inválido, tente novamente'
    def getDescricao(self):
        return self.__descricao
    
    def setDescricao(self,novaDescricao):
        if len(novaDescricao) < 256:
            self.__descricao = novaDescricao
        else:
            'Não foi possível modificar a descrição'
