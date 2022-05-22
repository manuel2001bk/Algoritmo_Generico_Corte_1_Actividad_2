class Individuo:
    def __init__(self, lista_paquetes):
        self.lista_paquetes = lista_paquetes
        self.peso_total = 0
        self.ganancia_total = 0
        self.posicion_valido = 0

    def __repr__(self):
        return repr((self.lista_paquetes, self.peso_total, self.ganancia_total, self.posicion_valido))