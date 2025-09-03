class Carro:
    def __init__(self,aro:int,cor:str,modelo:str,marca:str,ano:int,v = 0):
        '''
        Defina as variáveis iniciais do carro!
        aro: Forneça o aro do carro, exemplo: 14,15,16,18...
        '''
        self.aro = aro
        self.cor = cor
        self.modelo = modelo
        self.marca = marca
        self.v = v
        self.ano = ano
    def acelerar(self,velocidade):
        self.v += velocidade
        return self.v 
    def frear(self):
        if self.v == 0:
            return 'Carro Parado'
        else:
            self.v -= 5
            return self.v