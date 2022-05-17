class Individuo:
    def __init__(self, lista_paquetes, peso_total, ganancia_total):
        self.lista_paquetes = lista_paquetes
        self.peso_total = peso_total
        self.ganancia_total = ganancia_total

    def __repr__(self):
        return repr((self.lista_paquetes, self.peso_total, self.ganancia_total))