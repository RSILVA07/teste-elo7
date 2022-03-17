#Definir tamanho do espaço de locomoção da sonda

class Planalto:
    Min_Lrg = 0
    Min_Alt = 0

    def __init__ (self, lrg, alt, min_lrg=0, min_alt=0):
        self.lrg = lrg
        self.alt = alt
        self.Min_Lrg = min_lrg
        self.Min_Alt = min_alt

    def movimento (self,posicao):
        return self.Min_Lrg <= posicao.x <= self.lrg and self.Min_Alt <= posicao.y <= self.alt


#Definir posição inicial

class Posicao:
    x = 0
    y = 0

    def __init__ (self, x=0,y=0):
        self.x = x
        self.y = y

    def __eq__(self, posicao):
        return self.x == posicao.x and self.y == posicao.y
            

#Definir a movimentação da sonda com direção e pontos cardinais

class Sonda:

    COMANDOS = {
        'M': 'move',
        'L': 'left',
        'R': 'right',
    }

    def __init__(self)

