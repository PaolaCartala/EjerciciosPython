"""
Retomamos el dataset del arbolado porteño (arbolado-en-espacios-verdes.csv) para hacer algunos gráficos que nos permitan visualizar los datos.
- Generá un histograma con las alturas de los Jacarandás en el dataset.
- Escribí una función scatter_hd(lista_de_pares) que a partir de una lista de pares genere un scatterplot para visualizar la relación entre altura y diámetro de los Jacarandás del dataset.
- Hacé tres gráficos como en el ejercicio anterior, uno por cada especie.
"""

import csv
import os
import matplotlib.pyplot as plt
import numpy as np

# Funciones necesarias de la Clase 04
def leer_arboles(nombre_archivo):
    """
    Devuelve una lista de diccionarios con TODOS los arboles del archivo
    """
    f = open(nombre_archivo, encoding="utf8")
    rows = csv.reader(f)
    header = next(rows)
    arboleda = []
    for n_row, row in enumerate(rows, start=1):
        fuente = dict(zip(header, row))
        arboleda.append(fuente)
    return arboleda

arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')

# Devuelve las alturas de los arboles si son jacaranda
h = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']

# Devuelve una tupla con los valores de altura y diametro de los jacaranda
j = [tuple((float(arbol['altura_tot']), int(arbol['diametro']))) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']

def medidas_de_especies(especies, arboleda):
    """
    Devuelve un diccionario con cada {especie: [(altura, diametro)]}
    """
    diccionario = { especie: [tuple((float(arbol['altura_tot']), int(arbol['diametro']))) for arbol in arboleda if arbol['nombre_com'] == especie] for especie in especies }
    return diccionario 

medidas_de_especies(['Eucalipto', 'Palo borracho rosado', 'Jacarandá'], arboleda)

# Histograma de altos de Jacarandas
nombre_archivo = os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles(nombre_archivo)
altos = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
plt.title(f"Histograma de alturas de los Jacarandá")
plt.ylabel("alto (m)")
plt.xlabel("cantidad")
plt.hist(altos,bins=35)
plt.show()

# Scatterplot (diámetro vs alto) de Jacarandás
def scatter_hd(lista_de_pares):
    """
    Genera un gráfico de dispersión de la altura y dimensión de los Jacarandá.
    """
    convertida = np.array(lista_de_pares)
    d = [] # altura
    h = [] # diametro
    for x, y in convertida:
        d.append(x)
        h.append(y)
    colors = np.random.rand(len(convertida))
    area = (15 * np.random.rand(len(convertida))) ** 2
    plt.scatter(d, h, s=area, c=colors, alpha=0.7)
    plt.ylabel("diametro (cm)")
    plt.xlabel("alto (m)")
    plt.title("Relación diámetro-alto para Jacarandás")
    plt.show()

scatter_hd(j)

# Scatterplot para diferentes especies
# Itera sobre la lista especies y aplica la lógica
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
medidas = medidas_de_especies(especies, arboleda)
for especie in especies:
    convertida = np.array(medidas[especie])
    d = [] # altura
    h = [] # diametro
    for x, y in convertida:
        d.append(x)
        h.append(y)
    colors = np.random.rand(len(convertida))
    area = (15 * np.random.rand(len(convertida))) ** 2
    plt.scatter(d, h, s=area, c=colors, alpha=0.7)
    plt.ylabel("diametro (cm)")
    plt.xlabel("alto (m)")
    plt.title(f"Relación diámetro-alto para {especie}")
    plt.show()

