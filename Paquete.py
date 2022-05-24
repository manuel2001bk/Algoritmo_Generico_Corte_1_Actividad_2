class Paquete:
    def __init__(self, tipo, espacio, precio_publico,costo_envio,ganancia):
        self.tipo = tipo
        self.espacio = espacio
        self.precio_publico = precio_publico
        self.costo_envio = costo_envio
        self.ganancia = ganancia

    def __repr__(self):
        return repr((self.tipo, self.espacio, self.precio_publico, self.costo_envio, self.ganancia))