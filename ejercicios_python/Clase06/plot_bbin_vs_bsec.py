"""
Usando experimento_secuencial_promedio(lista, m, k) como base, escribí una función experimento_binario_promedio(lista, m, k) que cuente la cantidad de comparaciones que realiza en promedio (entre k experimentos elementales) la búsqueda binaria sobre la lista pasada como parámetro.
Graficá los resultados de estos experimentos para listas de largo entre 1 y 256.
Graficá ambas curvas en una misma figura, nombrando adecuadamente las curvas, los ejes y la figura completa. Jugá con xlim e ylim para visualizar bien las dos curvas, aunque tengas que restringir el rango.
"""

import random
import matplotlib.pyplot as plt
import numpy as np
import busqueda_en_listas as bl

m = 10000
n = 100
lista = bl.generar_lista(n, m)

# Acá comienza el experimento
# Experimento numérico (tiene una componente aleatoria)
# Experimento de promedios (calcula el promedio de comparaciones)
k = 1000

def experimento_secuencial_promedio(lista, m, k):
    """
    Retorna la cantidad de comparaciones promedio en k experimentos elementales
    """
    comps_tot = 0
    for i in range(k): # por cada experimento en la cantidad total de experimentos
        x = bl.generar_elemento(m) # generamos un elemento entre 0 y m
        comps_tot += bl.busqueda_secuencial_(lista,x)[1] # y lo buscamos en la lista, cuando lo encuentre o no, la funcion busqueda secuencial devolvera la cantidad de comparaciones que hizo y las sumará al total
    comps_prom = comps_tot / k # ese total de comparaciones se dividirá en la cantidad de experimentos que se quieren hacer
    return comps_prom # devolverá el promedio

def experimento_binario_promedio(lista, m, k):
    """
    Cuenta la cantidad de comparaciones que realiza la búsqueda binaria sobre la lista
    """
    comps_tot = 0
    for i in range(k): # por cada experimento en la cantidad total de experimentos
        x = bl.generar_elemento(m) # generamos un elemento entre 0 y m
        comps_tot += bl.busqueda_binaria(lista,x)[1] # y lo buscamos en la lista, cuando lo encuentre o no, la funcion busqueda binaria devolvera la cantidad de comparaciones que hizo y las sumará al total
    comps_prom = comps_tot / k # ese total de comparaciones se dividirá en la cantidad de experimentos que se quieren hacer
    return comps_prom # devolverá el promedio

# Graficamos los resultados de los experimentos de promedios para diferentes listas de largos n entre 1 y 256
m = 10000 # rango de numeros
k = 1000 # cantidad de experimentos

largos = np.arange(256) + 1 # estos son los largos de listas que voy a usar
comps_promedio = np.zeros(256) # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.
compas_promedio = np.zeros(256) # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.

for i, n in enumerate(largos):
    lista = bl.generar_lista(n, m) # genero lista de largo n
    comps_promedio[i] = experimento_secuencial_promedio(lista, m, k) # guardo el promedio del experimento secuencial en cada posicion i del array
    compas_promedio[i] = experimento_binario_promedio(lista, m, k)

# print(f'Secuencial: {comps_promedio}')
# print(f'Binaria: {compas_promedio}')

def graficar_bbin_vs_bseq(comps_promedio, compas_promedio):
    """
    Grafica los largos de listas con operaciones promedio de búsqueda tanto secuencial como binaria
    """
    plt.plot(largos,comps_promedio,label = 'Búsqueda Secuencial')
    plt.plot(largos,compas_promedio,label = 'Búsqueda Binaria')
    plt.xlabel("Largo de la lista")
    plt.ylabel("Cantidad de comparaciones")
    plt.title("Complejidad de la Búsqueda")
    plt.xlim([0, 20])
    plt.ylim([0, 20])
    plt.legend()
    plt.show()

graficar_bbin_vs_bseq(comps_promedio, compas_promedio)