import math
from ventana_ui import *

from Paquete import Paquete
from Individuo import Individuo

from random import Random, randint, random
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
        self.max_contenedor = 0
        self.num_div = 0
        self.parejas = []
        self.puntos_cruza = []
        self.porsentaje_descendencia = 0
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
            self.lista_individuos.append(Individuo(lista))

        print(self.lista_individuos)

    def cal_espacio(self):
        for i in range(len(self.lista_individuos)):
            suma_espacio = 0
            suma_ganancia = 0
            for y in range(len(self.lista_individuos[i].lista_paquetes)):
                indiv = self.lista_individuos[i].lista_paquetes[i]
                suma_espacio += indiv.espacio
                suma_ganancia += indiv.ganancia
                if suma_espacio < self.max_contenedor:
                    self.lista_individuos[i].peso_total = suma_espacio
                    self.lista_individuos[i].ganancia_total = suma_ganancia
                    self.lista_individuos[i].posicion_valido = y
        print(self.lista_individuos)

    def cal_div(self):
        self.num_div = len(self.lista_individuos)
        self.num_div = int(self.num_div/2)
        print("Numero de division: ", self.num_div)

    def crear_parejas(self):
        for i in range(self.num_div):
            for y in range(i+1, len(self.lista_individuos)):
                print("PAREJAS: i ", i, " : y ", y)
                self.parejas.append(
                    [self.lista_individuos[i], self.lista_individuos[y]])
        print("Lista parejas", self.parejas)

    def get_hijo(self, puntos_cruza, padre1, padre2):
        hijo = []
        for i in range(len(puntos_cruza)):
            for y in range(puntos_cruza[i]):
                if y < puntos_cruza[i]:
                    hijo.append(padre1.lista_paquetes[y])
                else:
                    hijo.append(padre2.lista_paquetes[y])
        return hijo

    def gen_cruza(self):
        puntos_cruza = random.sample(
            range(len(self.lista_paquetes)-1), k=randint(1, 5))
        puntos_cruza = sorted(puntos_cruza)
        print("Puntos de cruza: ", puntos_cruza)
        hijos = []
        for i in range(len(self.parejas)):
            print("Hijo generado")
            pareja = self.parejas[i]
            padre1 = pareja[0]
            padre2 = pareja[1]

            hijo = self.get_hijo(puntos_cruza,padre1, padre2)
            print("Hijo 1: ", hijo)
            # hijos.append(Individuo(hijo))
            # hijo = get_hijo(puntos_cruza, padre2, padre1)
            # print("Hijo 1: ", hijo)
            # hijos.append(Individuo(hijo))

    def cal_prob(self,pors):
        probabilidad = random()
        if probabilidad < pors:
            return True
        else:
            return False

    def algoritmo(self):
        print("Ingreso a metodo analizar algoritmo")
        self.cant_max_paquetes = int(self.cantidad_maxima_paquetes.text())
        self.gen__list_paquetes()
        self.conver_list_paquetes()
        self.pobla_init = int(self.poblacion_inicial.text())
        self.max_contenedor = int(self.tam_contenedor_max.text())
        self.porsentaje_descendencia = float(self.pors_desc.text())
        print(self.pobla_init)
        self.gen_individuos()
        print(self.lista_paquetes)
        self.cal_espacio()
        self.lista_individuos = sorted(
            self.lista_individuos, key=lambda genoma: genoma.peso_total, reverse=True)
        self.cal_div()
        print("Lista individuos ordenada", self.lista_individuos)
        self.crear_parejas()
        self.gen_cruza()

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
