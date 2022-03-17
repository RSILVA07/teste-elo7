#Definir tamanho do espaço de locomoção da sonda

class Planalto:
    Min_Lrg = 0
    Min_Alt = 0

    def __init__ (self, lrg, alt, min_lrg=0, min_alt=0):
        self.lrg = lrg
        self.alt = alt
        self.Min_Lrg = min_lrg
        self.Min_Alt = min_alt

#Definir posição inicial

#Definir a movimentação da sonda com direção e pontos cardinais
