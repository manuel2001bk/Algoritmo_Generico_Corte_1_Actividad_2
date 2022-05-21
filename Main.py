from turtle import st
from ventana_ui import *

from Paquete import Paquete
from Individuo import Individuo

from random import randint, random
import random


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.pors_desc
        self.pors_prob_ind
        self.pors_prob_gen
        self.num_gen
        self.poblacion_inicial
        self.poblacion_maxima
        self.paquete_tipo
        self.paquete_espacio
        self.paquete_ganancia
        self.cant_paquetes_label
        self.cantidad_maxima_paquetes
        self.tam_contenedor_max
        self.lista_tipo_paquetes = []
        self.lista_paquetes = []
        self.lista_individuos = []
        self.cant_max_paquetes = 0
        self.pobla_init = 0
        # Botones
        self.ingresar.clicked.connect(self.algoritmo)
        self.botton_ingresar_paquetes.clicked.connect(self.ingresar_paquete)

    def gen__list_paquetes(self):
        for i in range(self.cant_max_paquetes):
            self.lista_paquetes.append(
                randint(1, len(self.lista_tipo_paquetes)))
        self.lista_paquetes = sorted(self.lista_paquetes)
        print(self.lista_paquetes)

    def conver_list_paquetes(self):
        for i in range(len(self.lista_paquetes)):
            self.lista_paquetes[i] = self.lista_tipo_paquetes[self.lista_paquetes[i]-1]
        print(self.lista_paquetes)

    def gen_individuos(self):
        print(self.lista_paquetes)
        for i in range(self.pobla_init):
            lista = self.lista_paquetes.copy()
            random.shuffle(lista)
            self.lista_individuos.append(lista)
        
        print(self.lista_individuos)

    def algoritmo(self):
        print("Ingreso a metodo analizar algoritmo")
        self.cant_max_paquetes = int(self.cantidad_maxima_paquetes.text())
        self.gen__list_paquetes()
        self.conver_list_paquetes()
        self.pobla_init = int(self.poblacion_inicial.text())
        print(self.poblacion_inicial.text())
        self.gen_individuos()
        print(self.lista_paquetes)

        # print(self.pors_desc.text())
        # print(self.pors_prob_ind.text())
        # print(self.pors_prob_gen.text())
        # print(self.num_gen.text())
        # print(self.poblacion_maxima.text())

        # print(self.tam_contenedor_max.text())

    def ingresar_paquete(self):
        print("Ingreso a metodo generar paquete")
        tipo = self.paquete_tipo.text()
        espacio = int(self.paquete_espacio.text())
        ganancia = int(self.paquete_ganancia.text())
        print("Tipo : ", tipo, " Espacio : ",
              espacio, " Ganancia : ", ganancia)
        self.lista_tipo_paquetes.append(Paquete(tipo, espacio, ganancia))
        print(self.lista_tipo_paquetes)
        self.cant_paquetes_label.setText(
            "Tipos Paquetes ingresados : " + str(len(self.lista_tipo_paquetes)))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
