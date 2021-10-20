# -*- coding: utf-8 -*-
"""
mundo.py
Para jugar con el modelo, se puede modificar la instancia de Mundo (m) cambiando la cantidad de columnas y filas, así como la cantidad de leones y antílopes presentes.
Ejemplo:
> m = Mundo(15, 15, 15, 30, debug=True) tendrá un mundo de 15x15 con 15 leones y 30 antílopes, debug en True mostrará lo que va sucediendo en cada ciclo.
"""
#%%
from animal import Leon, Antilope
from tablero import Tablero

#%%
def print_debug(msg, print_flag=False):
    if print_flag:
        print(msg)

#%%
class Mundo(object):
    """docstring for Mundo"""

    def __init__(self, columnas, filas, n_leones, n_antilopes, debug=False):
        super(Mundo, self).__init__()

        self.debug = debug

        self.ciclo = 0
        self.tablero = Tablero(filas, columnas)
        self.llenar_mundo(n_leones, n_antilopes)


    def llenar_mundo(self, n_leones, n_antilopes):
        for _ in range(n_leones):
            if self.tablero.hay_posiciones_libres():
                print_debug("ubicando un leon", self.debug)
                self.tablero.ubicar_en_posicion_vacia(Leon())

        for _ in range(n_antilopes):
            if self.tablero.hay_posiciones_libres():
                print_debug("ubicando un Antilope", self.debug)
                self.tablero.ubicar_en_posicion_vacia(Antilope())

    def cant_leones(self):
        return sum([1 for x in self.tablero.elementos() if x.es_leon()])

    def cant_antilopes(self):
        return sum([1 for x in self.tablero.elementos() if x.es_antilope()])

    def etapa_movimiento(self):
        print_debug(f"Iniciando Movimiento en ciclo {self.ciclo}", self.debug)
        for p in self.tablero.posiciones_ocupadas(): 
            animal = self.tablero.posicion(p) 

            posiciones_libres = self.tablero.posiciones_vecinas_libre(p)
            nueva_posicion = animal.moverse(posiciones_libres)
            if nueva_posicion:
                self.tablero.mover(p, nueva_posicion)

    def etapa_alimentacion(self):
        print_debug(f"Iniciando Alimentación en ciclo {self.ciclo}", self.debug)
        for p in self.tablero.posiciones_ocupadas(): 
            animal = self.tablero.posicion(p) 
            animales_cercanos = self.tablero.posiciones_vecinas_con_ocupantes(p)
            desplazo = animal.alimentarse(animales_cercanos)
            if desplazo:
                self.tablero.ubicar(desplazo, self.tablero.retirar(p))

    def etapa_reproduccion(self):
        print_debug(f"Iniciando Reproducción en ciclo {self.ciclo}", self.debug)
        for p in self.tablero.posiciones_ocupadas(): # posiciones ocupadas lista de tuplas (fila, columna)
            animal = self.tablero.posicion(p) # p es la tupla (fila, columnas). en posicion elije el animal (fila, columnas): animal
            animales_cercanos = []
            for i in self.tablero.posiciones_vecinas_con_ocupantes(p):
                animales_cercanos.append(self.tablero.posicion(i[0]))
            pos = animal.reproducirse(animales_cercanos, self.tablero.posiciones_libres())
            if pos and animal.es_leon():
                self.tablero.ubicar(pos, Leon())
                print_debug(f'Nace un nuevo leoncito en la posición {pos}', self.debug)
            elif pos and animal.es_antilope():
                self.tablero.ubicar(pos, Antilope())
                print_debug(f'Nace un nuevo antílope en la posición {pos}', self.debug)
        # pass

    def cerrar_un_ciclo(self):
        print_debug(f"Concluyendo ciclo {self.ciclo}", self.debug)
        for p in self.tablero.posiciones_ocupadas():
            animal = self.tablero.posicion(p)
            animal.pasar_un_ciclo() #envejecer, consumir alimento
            if not animal.en_vida():
                self.tablero.retirar(p)
        self.ciclo += 1

    def pasar_un_ciclo(self):
        self.etapa_movimiento()
        self.etapa_alimentacion()
        self.etapa_reproduccion()
        self.cerrar_un_ciclo()


    def __repr__(self):
        res = str(self.tablero)
        res += f"\nEstamos en el ciclo {self.ciclo}"
        res += f"\nCon {self.cant_leones()} Leones, y {self.cant_antilopes()} Antilopes."
        if False:
            res += '\nEspecie   Posicion   años  energia   puede_reproduc\n'
            for p in self.tablero.posiciones_ocupadas():
                animal = self.tablero.posicion(p)
                res += f'{"Leon    " if animal.es_leon() else "Antilope"} {str(p):^10s} {animal.fila_str()}\n'

        return res

    def __str__(self):
        return self.__repr__()

# %%

m = Mundo(15, 15, 15, 30, debug=True)

import time
for i in range(20):
    m.pasar_un_ciclo()
    time.sleep(5)
    print(i +1)
    print(m)
# %%
