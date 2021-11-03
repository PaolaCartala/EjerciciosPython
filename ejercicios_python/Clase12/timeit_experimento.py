"""
Queremos evaluar cuánto tarda del método de ordenamiento por selección para diferentes longitudes de la lista a ordenar.
"""

#%%
import time
import timeit as tt
import numpy as np
from comparaciones_ordenamiento import generar_lista, ord_seleccion
import matplotlib.pyplot as plt

# generamos listas de longitudes entre 1 y 256
listas = []
for N in range(1, 256):
    listas.append(generar_lista(N))

#%%
def experimento_timeit_seleccion(listas, num):
    """
    Realiza un experimento usando timeit para evaluar el método de selección para ordenamiento de listas con las listas pasadas como entrada y devuelve los tiempos de ejecución para cada lista en un vector.
    El parámetro 'listas' debe ser una lista de listas.
    El parámetro 'num' indica el número de veces que repite el ordenamiento para cada lista.
    """
    tiempos_seleccion = []

    global lista

    for lista in listas:

        # evalúo el método de selección
        # en una copia nueva para cada iteración
        tiempo_seleccion = tt.timeit('ord_seleccion(lista.copy())', number = num, globals = globals())

        # guardo el resultado
        tiempos_seleccion.append(tiempo_seleccion)

    # paso los tiempos a arrays
    tiempos_seleccion = np.array(tiempos_seleccion)

    return tiempos_seleccion

#%%
# graficamos
tiempos_seleccion = experimento_timeit_seleccion(listas, 100)
plt.plot(tiempos_seleccion)
plt.show()
