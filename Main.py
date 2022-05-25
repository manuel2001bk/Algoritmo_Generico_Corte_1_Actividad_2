import math

from ventana_ui import *

from Paquete import Paquete
from Individuo import Individuo

from random import randint, random as random_2

import random

from matplotlib import pyplot as plt

from video import create_video


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.pors_prob_ind
        self.pors_prob_gen
        self.num_gen
        self.poblacion_inicial
        self.poblacion_maxima
        self.paquete_tipo
        self.paquete_espacio
        self.paquete_precio_publico
        self.paquete_costo_envio
        self.cantidad_paquetes
        self.cant_paquetes_label
        self.tam_contenedor_max
        self.lista_tipo_paquetes = []
        self.lista_paquetes = []
        self.lista_individuos = []
        self.generaciones = []
        self.cant_max_paquetes = 0
        self.pobla_init = 0
        self.max_contenedor = 0
        self.num_div = 0
        self.porsentaje_descendencia = 0
        self.maximo = []
        self.promedio = []
        self.minimo = []
        # Botones
        self.ingresar.clicked.connect(self.algoritmo)
        self.botton_ingresar_paquetes.clicked.connect(self.ingresar_paquete)
        self.generar_video.clicked.connect(self.genera_video_botton)

    def gen_individuos(self):
        print("Lista de paquetes: ", self.lista_paquetes)
        for i in range(self.pobla_init):
            lista = self.lista_paquetes.copy()
            random.shuffle(lista)
            self.lista_individuos.append(Individuo(lista))
        print("Lista de individuos generados: ", self.lista_individuos)

    def cal_espacio(self, lista):
        for i in range(len(lista)):
            suma_espacio = 0
            suma_ganancia = 0
            for y in range(len(lista[i].lista_paquetes)):
                individuo_unic = lista[i].lista_paquetes[y]
                suma_espacio += individuo_unic.espacio
                suma_ganancia += individuo_unic.ganancia
                if suma_espacio < self.max_contenedor:
                    lista[i].peso_total = suma_espacio
                    lista[i].ganancia_total = suma_ganancia
                    lista[i].posicion_valido = y
        print("Lista de individuos Despues de calculo de espacio: ", lista)
        return lista

    def cal_div(self):
        self.num_div = len(self.lista_individuos)
        self.num_div = math.ceil(self.num_div/2)
        print("Numero de division 50% mejores: ", self.num_div)

    def crear_parejas(self):
        parejas = []
        for i in range(self.num_div):
            for y in range(i+1, len(self.lista_individuos)):
                print("PAREJAS: i = ", i, " : y = ", y)
                parejas.append(
                    [self.lista_individuos[i], self.lista_individuos[y]])
        print("Lista parejas: ", parejas)
        return parejas

    def get_hijo(self, puntos_cruza, padre1, padre2):
        hijo = []
        for i in range(puntos_cruza[0]):
            hijo.append(padre1.lista_paquetes[i])

        for i in range(puntos_cruza[0], puntos_cruza[1]):
            hijo.append(padre2.lista_paquetes[i])

        for i in range(puntos_cruza[1], len(padre1.lista_paquetes)):
            hijo.append(padre1.lista_paquetes[i])
        return Individuo(hijo)

    def comprobar_repetidos(self, hijo, padre):
        mylist = hijo.lista_paquetes
        resultant_list = []

        for element in mylist:
            if element not in resultant_list:
                resultant_list.append(element)
        mylist = resultant_list
        for element in padre.lista_paquetes:
            if element not in mylist:
                mylist.append(element)
        return mylist

    def generar_cruza(self, parejas):
        hijos = []
        for i in range(len(parejas)):
            puntos_cruza = random.sample(
                range(1, len(self.lista_paquetes)-2), k=2)
            puntos_cruza = sorted(puntos_cruza)
            print("Puntos de cruza: ", puntos_cruza)
            print("Hijo generado")
            pareja = parejas[0]
            padre1 = pareja[0]
            padre2 = pareja[1]

            hijo = self.get_hijo(puntos_cruza, padre1, padre2)
            print("Hijo 1: ", hijo)
            print("Padre : ", padre1)
            print("Madre : ", padre2)

            hijos.append(Individuo(self.comprobar_repetidos(hijo, padre2)))
            hijo = self.get_hijo(puntos_cruza, padre2, padre1)
            print("Hijo 1: ", hijo)
            print("Padre : ", padre2)
            print("Madre : ", padre1)
            hijos.append(Individuo(self.comprobar_repetidos(hijo, padre1)))
        return hijos

    def cal_prob(self, pors):
        probabilidad = random_2()
        if probabilidad < pors:
            return True
        else:
            return False

    def mutacion_genetica(self, hijo):
        for i in range(len(hijo.lista_paquetes)):
            if self.cal_prob(float(self.pors_prob_gen.text())):
                posicion = randint(i, len(hijo.lista_paquetes)-1)
                aux = hijo.lista_paquetes[i]
                hijo.lista_paquetes[i] = hijo.lista_paquetes[posicion]
                hijo.lista_paquetes[posicion] = aux
        return hijo

    def mutacion_ind(self, hijos):
        for i in range(len(hijos)):
            if self.cal_prob(float(self.pors_prob_ind.text())):
                hijos[i] = self.mutacion_genetica(hijos[i])
        return hijos

    def poda_mejores(self):
        self.lista_individuos = self.lista_individuos[0:int(
            self.poblacion_maxima.text())]

    def calculo_promedio(self, lista):
        suma = 0
        for i in range(len(lista)):
            suma += lista[i].ganancia_total
        suma = suma/len(lista)
        self.promedio.append(suma)

    def algoritmo(self):
        print("Ingreso a metodo analizar algoritmo")
        self.pobla_init = int(self.poblacion_inicial.text())
        self.max_contenedor = int(self.tam_contenedor_max.text())
        self.gen_individuos()
        self.generaciones.append(self.lista_individuos.copy())
        # print("Lista de paquetes despues de generar individuos: ",
        #       self.lista_paquetes)
        self.lista_individuos = self.cal_espacio(self.lista_individuos)

        self.lista_individuos = sorted(
            self.lista_individuos, key=lambda genoma: genoma.ganancia_total, reverse=True)
        self.cal_div()
        self.calculo_promedio(self.lista_individuos)
        self.maximo.append(self.lista_individuos[0].ganancia_total)
        self.minimo.append(self.lista_individuos[len(
            self.lista_individuos)-1].ganancia_total)

        print("Lista individuos ordenada", self.lista_individuos)
        for i in range(int(self.num_gen.text())):
            self.lista_individuos = sorted(
                self.lista_individuos, key=lambda genoma: genoma.peso_total, reverse=True)
            print("Generacion : ", i)
            parejas = self.crear_parejas()
            hijos = self.generar_cruza(parejas)
            print("Hijos despues de cruza: ", hijos)
            hijos = self.mutacion_ind(hijos)
            print("Hijos despues de Mutacion: ")
            print(hijos)
            hijos = self.cal_espacio(hijos)
            print("Hijos despues de calculo de ganancia: ")
            print(hijos)
            for y in range(len(hijos)):
                self.lista_individuos.append(hijos[y])

            self.lista_individuos = sorted(
                self.lista_individuos, key=lambda genoma: genoma.ganancia_total, reverse=True)
            print("Lista de poblacion antes de poda:")
            print(self.lista_individuos)
            self.calculo_promedio(self.lista_individuos)
            self.maximo.append(self.lista_individuos[0].ganancia_total)
            self.minimo.append(self.lista_individuos[len(
                self.lista_individuos)-1].ganancia_total)
            self.poda_mejores()
            print("Lista de poblacion despues de poda:")
            print(self.lista_individuos)
            self.generaciones.append(self.lista_individuos.copy())
            

        self.tabla_historial()
        self.tabla_generaciones()

    def tabla_generaciones(self):
        fig2 = plt.figure(figsize=(10, 5))
        fig2.tight_layout()
        plt.style.use('_mpl-gallery')
        plt.subplots_adjust(left=0.06, right=0.95, bottom=0.06, top=0.95)

        for x in range(len(self.generaciones)):
            aptitudes = self.generaciones[x]
            aptitud_x = []
            aptitud_generacion = []
            for i in range(len(aptitudes)):
                aptitud_x.append(i+1)
                aptitud_generacion.append(aptitudes[i].ganancia_total)
            ax_2 = plt.subplot(1, 1, 1)
            ax_2.barh(aptitud_x, aptitud_generacion)
            ax_2.set_xlabel("Ganancia Total")
            ax_2.set_ylabel("Paquetes")
            ax_2.set_title("Generacion "+str(x+1) + "°")
            num_gen = x + 1
            if num_gen < 10:
                name = f'0{num_gen}'
            elif num_gen >= 10 and num_gen < 100:
                name = f'{x+1}'
            elif num_gen >= 100 and num_gen < 1000:
                name = f'c_{num_gen}'
            plt.savefig(f'imgs/{name}.png')

    def tabla_historial(self):
        x = []
        fig = plt.figure(figsize=(10, 5))
        fig.tight_layout()
        plt.style.use('_mpl-gallery')
        for i in range(len(self.maximo)):
            x.append(i+1)
        ax = plt.subplot(1, 1, 1)
        ax.plot(x, self.maximo, label='Caso Máximo')
        ax.plot(x, self.promedio, label='Caso Promedio')
        ax.plot(x, self.minimo, label='Caso Mínimo')
        ax.legend(loc='upper right')
        plt.savefig(f'imgs/historico.png')
        plt.show()

    def ingresar_paquete(self):
        print("Ingreso a metodo generar paquete")
        tipo = self.paquete_tipo.text()
        espacio = int(self.paquete_espacio.text())
        precio_publico = int(self.paquete_precio_publico.text())
        costo_envio = int(self.paquete_costo_envio.text())
        cantidad_paquetes = int(self.cantidad_paquetes.text())
        ganancia = precio_publico-costo_envio
        print("Tipo : ", tipo, " Espacio : ",
              espacio, " Precio Publico : ", precio_publico)
        print(" Costo envio : ", costo_envio,
              " Cantidad paquetes : ", cantidad_paquetes)
        self.lista_tipo_paquetes.append(
            Paquete(tipo, espacio, precio_publico, costo_envio, ganancia))
        for i in range(cantidad_paquetes):
            self.lista_paquetes.append(
                Paquete((tipo+str(i+1)), espacio, precio_publico, costo_envio, ganancia))
        print(self.lista_paquetes)
        print(self.lista_tipo_paquetes)
        self.cant_paquetes_label.setText(
            "Tipos Paquetes ingresados : " + str(len(self.lista_tipo_paquetes)))
    def genera_video_botton(self):
        create_video()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
