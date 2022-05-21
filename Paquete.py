class Paquete:
    def __init__(self, tipo, espacio, ganancia):
        self.tipo = tipo
        self.espacio = espacio
        self.ganancia = ganancia

    def __repr__(self):
        return repr((self.tipo, self.espacio, self.ganancia))