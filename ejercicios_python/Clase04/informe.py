"""
Supongamos que los precios en camion.csv son los precios pagados al productor de frutas mientras que los precios en precios.csv son los precios de venta en el lugar de descarga del camión.
- Tratá de escribir los comandos adecuados para realizar las operaciones descriptas abajo. Estas operaciones son reducciones, transformaciones y consultas sobre la carga del camión.
- Calculá el costo total de la carga del camión en un solo comando. Luego, leyendo la variable precios, calculá también el valor en el mercado de la carga del camión usando una sola línea de código.
- Primero, generá una lista con la info de todas las frutas que tienen más de 100 cajones en el camión. Ahora, una con la info sobre cajones de Mandarina y Naranja. O una con la info de las frutas que costaron más de $10000. Esta forma de escribir resulta análoga a las consultas a una base de datos con SQL.
- Usando un comprensión de listas, construí una lista de tuplas (nombre, cajones) que indiquen la cantidad de cajones de cada fruta tomando los datos de camion. Si cambiás los corchetes ([ , ]) por llaves ({ , }), obtenés algo que se conoce como comprensión de conjuntos. Vas a obtener valores únicos.
"""

import csv

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

datos_camion = leer_camion('../Data/camion.csv')

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

# Reduccion de secuencias
camion = leer_camion('../Data/fecha_camion.csv')
costo = sum([s['cajones'] * s['precio'] for s in camion])
print(costo)

precios = leer_precios('../Data/precios.csv')
valor = sum(s['cajones'] * precios[s['nombre']] for s in camion)
print(valor)

# Consultas de datos
print('mas100')
mas100 = [s for s in camion if s['cajones'] > 100]
print(mas100)

print('myn')
myn = [s for s in camion if s['nombre'] in {'Mandarina', 'Naranja'}]
print(myn)

print('costo10k')
costo10k = [s for s in camion if s['cajones'] * s['precio'] > 10000]
print(costo10k)

# Extraccion de datos
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