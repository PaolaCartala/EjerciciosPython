"""
El archivo ../Data/camion.csv contiene la lista de cajones cargados en un camión. Definí una función leer_camion(nombre_archivo) que abre un archivo con el contenido de un camión, lo lee y devuelve la información como una lista de diccionarios.
Escribí una función leer_precios(nombre_archivo) que a partir de un conjunto de precios arme un diccionario donde las claves sean los nombres de frutas y verduras, y los valores sean los precios por cajón.
Supongamos que los precios en camion.csv son los precios pagados al productor de frutas mientras que los precios en precios.csv son los precios de venta en el lugar de descarga del camión.
- Ahora vamos calcular el balance del negocio
"""

import csv
from collections import Counter

def leer_camion(nombre_archivo):
    """
    Abre el archivo nombre_archivo, salta su encabezado, lee las lineas subsiguientes y arma una lista de diccionarios con los datos de cada nombre, cajones y precio.
    """
    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        header = next(rows)
        camion = []
        lote = {}
        for n_row, row in enumerate(rows, start=1):
            fuente = dict(zip(header, row))
            lote = {'nombre': fuente['nombre'], 
                'cajones': int(fuente['cajones']), 
                'precio': float(fuente['precio']),
            }
            camion.append(lote)
    return camion

datos_camion = leer_camion('../Data/fecha_camion.csv')

def leer_precios(nombre_archivo):
    """
    Devuelve un diccionario {'nombre de frutas': precio por cajon}
    """
    precios = {}
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        try:
            for row in rows:
                precios[row[0]] = float(row[1])
        except:
            return precios
    return precios

precios_venta = leer_precios('../Data/precios.csv')

def costo_camion(camion):
    """
    Devuelve el costo de las frutas que están presentes en el camión y en la lista de precios
    """
    total_camion = 0
    for i in camion:
        total_camion += i['cajones'] * i['precio']
    return total_camion

costo_camion = costo_camion(datos_camion)

def ventas(precios, camion):
    """
    Devuelve el total de ventas
    """
    total_ventas = 0
    for p in camion:
        for f in precios:
            if f == p['nombre']:
                total_ventas += precios[f] * p['cajones']
    return total_ventas

# Balance del negocio
ventas = ventas(precios_venta, datos_camion)

diferencia = ventas - costo_camion

print(f"La ganancia en ventas es de ${round(diferencia, 2)}")