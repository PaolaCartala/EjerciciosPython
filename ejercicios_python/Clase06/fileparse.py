"""
Crea la función parse_csv que lee un archivo CSV y arma una lista de diccionarios a partir del contenido del archivo CSV.
- Modifiquemos la función parse_csv de modo que permita al usuario elegir (opcionalmente) algunas columnas.
- Modificá la función de modo que permita, opcionalmente, convertir el tipo de los datos recuperados antes de devolverlos.
- Modificá la función parse_csv() de forma que (opcionalmente) pueda trabajar con este tipo de archivos, creando tuplas en lugar de diccionarios cuando no haya encabezados.
"""

import csv

def parse_csv(nombre_archivo, select=None, types=None, has_headers=True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar (select) sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    Se puede convertir el tipo de datos pasando una lista de tipos en type.
    Se puede elegir entre archivos con encabezados (has_headers) devolviendo una lista de diccionarios o archivos sin encabezados devolviendo una lista de tuplas.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)
        if has_headers:
            # Lee los encabezados del archivo
            encabezados = next(filas)

            # Si se indicó un selector de columnas,
            #    buscar los índices de las columnas especificadas.
            # Y en ese caso achicar el conjunto de encabezados para diccionarios

            if select:
                indices = [encabezados.index(nombre_columna) for nombre_columna in select]
                encabezados = select
            else:
                indices = []

            registros = []
            for fila in filas:
                if not fila:    # Saltear filas vacías
                    continue
                # Filtrar la fila si se especificaron columnas
                if indices:
                    fila = [fila[index] for index in indices]
                if types:
                    fila = [func(val) for func, val in zip(types, fila) ]
                # Armar el diccionario
                registro = dict(zip(encabezados, fila))
                registros.append(registro)
        else:
            registros = []
            for fila in filas:
                if not fila:    # Saltear filas vacías
                    continue
                # Filtrar la fila si se especificaron columnas
                if select:
                    fila = [fila[index] for index in select]
                if types:
                    fila = [func(val) for func, val in zip(types, fila)]
                # Armar la tupla
                registro = tuple(fila)
                registros.append(registro)

    return registros

# Retorna una lista de diccionarios [{'nombre', 'cajones', 'precio'}]
camion = parse_csv('../Data/camion.csv', types=[str, int, float], has_headers=True, select=['nombre', 'cajones', 'precio'])
# Retorna una lista de tuplas [('nombre', precio)]
precios = parse_csv('../Data/precios.csv', types=[str, float], has_headers=False)

# print(camion)
# print(precios)
