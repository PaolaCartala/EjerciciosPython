"""
El objetivo de esta actividad es hacer un programa en Python que responda la pregunta: ¿Cuántas figuritas hay que comprar para completar el álbum del Mundial?
Datos:
Álbum con 670 figuritas.
Cada figurita se imprime en cantidades iguales y se distribuye aleatoriamente.
Cada paquete trae cinco figuritas.
- Suponé por ahora que las figuritas se compran individualmente (no en un paquete con cinco). En este caso, la dinámica del llenado es la siguiente:
Iniciamos con un álbum vacío y sin haber comprado ninguna figurita.
Compramos figuritas (de a una) hasta llenar el álbum; es decir, se repite la acción (el paso) de comprar y pegar figuritas mientras el álbum está incompleto.
Al terminar nos interesa saber cuántas figuritas tuvimos que comprar para llenar el álbum.
- Implementá la función album_incompleto(A) que recibe un vector y devuelve True si el álbum A no está completo y False si está completo.
- Implementá una función comprar_figu(figus_total) que reciba el número total de figuritas que tiene el álbum (dado por el parámetro figus_total) y devuelva un número entero aleatorio que representa la figurita que nos tocó.
- Ejecutá n_repeticiones = 1000 veces la función anterior utilizando figus_total = 6 y guardá en una lista los resultados obtenidos en cada repetición. Con los resultados obtenidos estimá cuántas figuritas hay que comprar, en promedio, para completar el álbum de seis figuritas.
- Escribí una función llamada experimento_figus(n_repeticiones, figus_total) que simule el llenado de n_repeticiones álbums de figus_total figuritas y devuelva el número estimado de figuritas que hay que comprar, en promedio, para completar el álbum.
Ahora con paquetes
- Simulá la generación de un paquete con cinco figuritas, sabiendo que el álbum es de 670. Tené en cuenta que, como en la vida real, puede haber figuritas repetidas en un paquete.
- Implementá una función comprar_paquete(figus_total, figus_paquete) que, dado el tamaño del álbum (figus_total) y la cantidad de figuritas por paquete (figus_paquete), genere un paquete (lista) de figuritas al azar.
- Implementá una función cuantos_paquetes(figus_total, figus_paquete) que dado el tamaño del álbum y la cantidad de figus por paquete, genere un álbum nuevo, simule su llenado y devuelva cuántos paquetes se debieron comprar para completarlo.
- Calculá n_repeticiones = 100 veces la función cuantos_paquetes, utilizando figus_total = 670, figus_paquete = 5. Guarda los resultados obtenidos en una lista y calculá su promedio.
- Graficar el llenado del álbum
"""

import random
import numpy as np
import matplotlib.pyplot as plt

def crear_album(figus_total):
    """
    Retorna un álbum con ceros según la cantidad pasada en figus_total
    """
    return np.zeros((1, figus_total))

def album_incompleto(A):
    """
    Evalúa si hay algún número 0 en el álbum, retorna True si existe un 0 (album incompleto) y False si están los lugares ocupados por otro número
    """
    if A.min() == 0:
        return True
    else:
        return False

def comprar_figu(figus_total):
    """
    Retorna un número aleatorio entre 1 y figus_total que representa una figurita
    """
    return random.randint(1, figus_total)

def cuantas_figus(figus_total):
    """
    Evalúa mientras el album esté incompleto cuantas compras hay que hacer para completarlo. Utilizando las funciones anteriores crea un album y crea una figurita, registra una compra y evalúa si la figurita no está y la agrega, pero si la figurita no está continúa. Retorna las compras cuando el while se evalúa como falso, es decir que el álbum está completo.
    """
    compras = 0
    album = crear_album(figus_total)
    while album_incompleto(album):
        figurita = comprar_figu(figus_total)
        compras += 1
        if album[0][figurita - 1] != figurita:
            album[0][figurita - 1] = figurita
        else:
            continue
    return compras

cuantas_figus(6)

# Ejecuta la funcion cuantas_figus() 1000 veces y las agrega a la lista total, luego saca el promedio
total = []
[total.append(cuantas_figus(6)) for _ in range(1000)]
promedio = np.mean(total)

def experimento_figus(n_repeticiones, figus_total):
    total = []
    [total.append(cuantas_figus(figus_total)) for _ in range(n_repeticiones)]
    promedio = np.mean(total)
    return promedio

experimento_figus(100, 670)

# Simula la generación de un paquete
paquete = []
for _ in range(5):
    paquete.append(comprar_figu(670))
print(paquete)

def comprar_paquete(figus_total, figus_paquete):
    """
    Agrega figuritas y devuelve una lista con figus_paquete cantidad de figuritas
    """
    paquete = []
    for _ in range(figus_paquete):
        paquete.append(comprar_figu(figus_total))
    return paquete

def cuantos_paquetes(figus_total, figus_paquete):
    """
    Evalúa cuantos paquetes se necesitan para completar el álbum iterando sobre el paquete y evaluando cada figurita
    """
    compras = 0
    album = crear_album(figus_total)
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        for figurita in paquete:
            if album[0][figurita - 1] != figurita:
                album[0][figurita - 1] = figurita
            else:
                continue
        compras += 1
    return compras

cuantos_paquetes(670, 5)

# CUIDADO: comenzar a evaluar con un range(100) para no sobrecargar la memoria
total = []
[total.append(cuantos_paquetes(670, 5)) for _ in range(1000)]
promedio = np.mean(total)
print(promedio)