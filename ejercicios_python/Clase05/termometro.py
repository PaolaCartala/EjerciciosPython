"""
Supongamos que una persona se compra un termómetro que mide la temperatura con un error aleatorio de distribución normal con media 0 y desvío estándar de 0.2 grados (error gaussiano). Si la temperatura real de la persona es de 37.5 grados, simulá usando normalvariate() (con mu y sigma adecuados) n valores medidos por el termómetro. 
- Escribí una función llamada medir_temp(n) que simule n mediciones y las devuelva en una lista.
- Escribí una función llamada resumen_temp(n) que realice una simulación de n temperaturas (usando la función medir_temp(n)) y devuelva una tupla con el valor máximo, el mínimo, el promedio y la mediana (en ese orden) de estas n mediciones.
- Crea un array con las mediciones según la cantidad de repeticiones que se pasan por parámetro y las guarda en el archivo temperaturas.npy
"""

import random
import numpy as np

# Gaussiana
def medir_temp(n):
    """
    Retorna las mediciones de temperatura según la temperatura real (37,5°C) de una persona, la media y desviación estándar.
    """
    mediciones = []
    for _ in range(n):
        temperatura = 37.5 + (random.normalvariate(0, 0.2))
        mediciones.append(temperatura)
    return mediciones

def resumen_temp(n):
    """
    Retorna una tupla con cada maximo, minimo, promedio y mediana de las mediciones
    """
    temperaturas = medir_temp(n)
    maximo = max(temperaturas)
    minimo = min(temperaturas)
    promedio = sum(temperaturas) / n
    ordenados = sorted(temperaturas)
    if len(ordenados) % 2 == 0:
        mitad = int(len(ordenados) / 2) - 1
        mediana = (ordenados[mitad] + ordenados[mitad + 1]) / 2
    else:
        mitad = int(len(ordenados) / 2)
        mediana = ordenados[mitad]
    return (maximo, minimo, promedio, mediana)

print(f'Máximo: {resumen_temp(999)[0]}\nMínimo: {resumen_temp(999)[1]}\nPromedio: {resumen_temp(999)[2]}\nMediana: {resumen_temp(999)[3]}')

# Guardar temperaturas
a = np.array(medir_temp(999))
np.save('../Data/temperaturas', a)