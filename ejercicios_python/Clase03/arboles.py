"""
Vamos a repasar las herramientas que vimos en esta clase aplicándolas a una base de datos sobre árboles en parques de la Ciudad de Buenos Aires.
- Definí una función leer_parque(nombre_archivo, parque) que abra el archivo indicado y devuelva una lista de diccionarios con la información del parque especificado. La lista debe tener un diccionario por cada árbol del parque elegido.
- Escribí una función especies(lista_arboles) que tome una lista de árboles como la generada en el ejercicio anterior y devuelva el conjunto de especies que figuran en la lista.
- Escribí una función contar_ejemplares(lista_arboles) que, dada una lista como la que generada con leer_parque(), devuelva un diccionario en el que las especies sean las claves y tengan como valores asociados la cantidad de ejemplares en esa especie en la lista dada. Luego, combiná esta función con leer_parque() y con el método most_common() para informar las cinco especies más frecuentes
- Escribí una función obtener_alturas(lista_arboles, especie) que, dada una lista de árboles como la anterior y una especie de árbol, devuelva una lista con las alturas de los ejemplares de esa especie en la lista.
- Escribí una función obtener_inclinaciones(lista_arboles, especie) que, dada una especie de árbol y una lista de árboles como la anterior, devuelva una lista con las inclinaciones de los ejemplares de esa especie.
"""

import csv
from collections import Counter

def leer_parque(nombre_archivo, parque):
    """
    Abre nombre_archivo y devuelva una lista de diccionarios con la información de parque.
    """
    f = open(nombre_archivo, encoding="utf8")
    rows = csv.reader(f)
    header = next(rows)
    informacion = []
    for n_row, row in enumerate(rows, start=1):
        fuente = dict(zip(header, row))
        if fuente['espacio_ve'] == parque:
            informacion.append(fuente)
    return informacion

leer_parque = leer_parque('../Data/arbolado-en-espacios-verdes.csv', "CENTENARIO")

def especies(lista_arboles):
    """
    Toma lista_arboles de leer_parque y devuelve el conjunto de especies de la lista
    """
    especies = set()
    for e in lista_arboles:
        especies.add(e['nombre_com'])
    return especies

especies = especies(leer_parque)

def contar_ejemplares(lista_arboles):
    """
    Devuelve las 5 especies más frecuentes en una lista de tuplas con el nombre del árbol y la cantidad
    """
    especie = Counter()
    for e in lista_arboles:
        especie[e['nombre_com']] += 1
    comunes = especie.most_common(5)
    return comunes

contar_ejemplares = contar_ejemplares(leer_parque)
print(contar_ejemplares)

def obtener_alturas(lista_arboles, especie):
    """
    Toma una lista de árboles y devuelve una lista con las alturas de los ejemplares de especie
    """
    arboles = []
    for n, l in enumerate(lista_arboles):
        if l['nombre_com'] == especie:
            arboles.append(float(lista_arboles[n]['altura_tot']))
    # print(max(arboles))
    # print(round(sum(arboles) / len(arboles), 2))
    return arboles

obtener_alturas(leer_parque, 'Jacarandá')

def obtener_inclinaciones(lista_arboles, especie):
    """
    Devuelve una lista con las inclinaciones de especie
    """
    inclinacion = []
    for n, l in enumerate(lista_arboles):
        if l['nombre_com'] == especie:
            inclinacion.append(int(lista_arboles[n]['inclinacio']))
    return inclinacion

obtener_inclinaciones = obtener_inclinaciones(leer_parque, 'Falso Guayabo (Guayaba del Brasil)')