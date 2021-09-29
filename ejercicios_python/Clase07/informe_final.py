#! python3

"""
Agregá a tu programa una función f_principal() que tome una lista de parámetros en la línea de comandos y produzca la misma salida que antes.
Para ejecutarlo en el símbolo del sistema (Windows) tenes que posicionarte en la carpeta Clase07 y correr la línea
> python informe_final.py ../Data/camion.csv ../Data/precios.csv
"""

import csv
import sys
import fileparse

def leer_camion(nombre_archivo):
    """
    Devuelve una lista de diccionarios con [{'nombre', 'cajones', 'precio'}] de cada item del archivo
    """
    with open(nombre_archivo) as file:
        camion = fileparse.parse_csv(file, types=[str, int, float], has_headers=True, select=['nombre', 'cajones', 'precio'])
    return camion

def leer_precios(nombre_archivo):
    """
    Devuelve un diccionario {'nombre':'precio'} de cada item del archivo de precios al consumidor
    """
    precios = {}
    with open(nombre_archivo) as file:
        lista = fileparse.parse_csv(file, types=[str, float], has_headers=False)
    try:
        for row in lista:
            precios[row[0]] = float(row[1])
    except:
        return precios
    return precios

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

def imprimir_informe(informe):
    """
    Imprime una tabla (informe) con el nombre de cada item, la cantidad de cajones, su precio unitario y la ganancia
    """
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print(f'{"-"*10} {"-"*10} {"-"*10} {"-"*10}')
    for nombre, cajones, precio, cambio in informe:
        print(f'{nombre:>10s} {cajones:>10d} {"$":>3s}{precio:>6.2f} {cambio:>10.2f}')

def f_principal(nombre_archivo_camion, nombre_archivo_precios):
    """
    Crea una función de alto nivel que ejecuta las funciones anteriores en un solo llamado
    """
    datos_camion = leer_camion(nombre_archivo_camion)
    precios_venta = leer_precios(nombre_archivo_precios)
    informe = hacer_informe(datos_camion, precios_venta)
    imprimir_informe(informe)

# if __name__ == '__main__':
#     f_principal(sys.argv[1], sys.argv[2])

files = ['../Data/camion.csv', '../Data/camion2.csv']
for name in files:
    print(f'{name:-^43s}')
    f_principal(name, '../Data/precios.csv')
    print()