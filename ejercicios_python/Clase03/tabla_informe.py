"""
Modifica el archivo informe.py para producir una tabla
"""

import csv

def leer_camion(nombre_archivo):
    """
    Devuelve una lista de diccionarios con [{'nombre', 'cajones', 'precio'}] de cada item del archivo
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
    Devuelve un diccionario {'nombre':'precio'} de cada item del archivo de precios al consumidor
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

def hacer_informe(lista_cajones, precios):
    """
    Devuelve una lista de tuplas con el nombre del item, la cantidad de cajones en enteros, su precio de costo en punto flotante y la diferencia entre el costo y el precio de venta en punto flotante
    """
    informe = []
    for p in lista_cajones:
        for f in precios:
            if f == p['nombre']:
                p['cambio'] = precios[f] - p['precio']
                informe.append(tuple(p.values()))
    return informe

informe = hacer_informe(datos_camion, precios_venta)

# Imprime una tabla con el nombre de cada item, la cantidad de cajones, su precio unitario y la ganancia
headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
print(f'{"-"*10} {"-"*10} {"-"*10} {"-"*10}')
for nombre, cajones, precio, cambio in informe:
    print(f'{nombre:>10s} {cajones:>10d} {"$":>3s}{precio:>6.2f} {cambio:>10.2f}')
