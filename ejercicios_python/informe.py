"""
Supongamos que los precios en camion.csv son los precios pagados al productor de frutas mientras que los precios en precios.csv son los precios de venta en el lugar de descarga del camión.
- Ahora vamos calcular el balance del negocio
"""

import csv
from collections import Counter

def leer_camion(nombre_archivo):
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

datos_camion = leer_camion('Data/fecha_camion.csv')

datos_camion2 = leer_camion('Data/camion2.csv')

tenencias = Counter()
for s in datos_camion:
    tenencias[s['nombre']] += s['cajones']

tenencias2 = Counter()
for s in datos_camion2:
    tenencias2[s['nombre']] += s['cajones']

print(tenencias.most_common(3))

combinadas = tenencias + tenencias2

def leer_precios(nombre_archivo):
    precios = {}
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        try:
            for row in rows:
                precios[row[0]] = float(row[1])
        except:
            return precios
    return precios

precios_venta = leer_precios('Data/precios.csv')
# print(precios_venta)

def costo_camion(camion):
    total_camion = 0
    for i in camion:
        total_camion += i['cajones'] * i['precio']
    return total_camion

costo_camion = costo_camion(datos_camion)

def ventas(precios, camion):
    total_ventas = 0
    for p in camion:
        for f in precios:
            if f == p['nombre']:
                total_ventas += precios[f] * p['cajones']
    return total_ventas

ventas = ventas(precios_venta, datos_camion)

diferencia = ventas - costo_camion

print(f"La ganancia en ventas es de ${round(diferencia, 2)}")

# 4.8 reduccion de secuencias
camion = leer_camion('Data/fecha_camion.csv')
costo = sum([s['cajones'] * s['precio'] for s in camion])
print(costo)

# 4.8 reduccion de secuencias
precios = leer_precios('Data/precios.csv')
valor = sum(s['cajones'] * precios[s['nombre']] for s in camion)
print(valor)

# 4.9 consultas de datos
print('mas100')
mas100 = [s for s in camion if s['cajones'] > 100]
print(mas100)

print('myn')
myn = [s for s in camion if s['nombre'] in {'Mandarina', 'Naranja'}]
print(myn)

print('costo10k')
costo10k = [s for s in camion if s['cajones'] * s['precio'] > 10000]
print(costo10k)

# 4.10 extraccion de datos
print('nombre_cajones')
nombre_cajones = {(s['nombre'], s['cajones']) for s in camion}
print(nombre_cajones)

print('listado de frutas')
nombres = {s['nombre'] for s in camion}
print(nombres)
stock = {nombre: 0 for nombre in nombres}
print(stock)
for s in camion:
    stock[s['nombre']] += s['cajones']
print(stock)

camion_precios = {nombre: precios[nombre] for nombre in nombres}
print(camion_precios)
