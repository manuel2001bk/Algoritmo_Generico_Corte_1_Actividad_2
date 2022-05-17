class Paquete:
    def __init__(self, identificador, peso, ganancia):
        self.identificador = identificador
        self.peso = peso
        self.ganancia = ganancia

    def __repr__(self):
        return repr((self.identificador, self.peso, self.ganancia))