"""
Modifcá tu código para que lance una excepción en caso que ambos parámetros select y has_headers = False sean pasados juntos.
Modificá la función parse_csv() de modo que atrape todas las excepciones de tipo ValueError generadas durante el armado de los registros a devolver e imprima un mensaje de advertencia para las filas que no pudieron ser convertidas.
Modificá parse_csv() de modo que el usuario pueda silenciar los informes de errores en el parseo de los datos que agregaste antes, con un parámetro silence_errors.
Actualmente la función solicita el nombre de un archivo, pero podés hacer el código más flexible. Modificá la función de modo que funcione con cualquier objeto o iterable que se comporte como un archivo.
"""

import csv

def parse_csv(nombre_archivo, select=None, types=None, has_headers=True, silence_errors = False):
    '''
    Parsea un iterable en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    Se puede convertir el tipo de datos pasando una lista de tipos en type.
    Se puede elegir entre archivos con encabezados (has_headers) devolviendo una lista de diccionarios o archivos sin encabezados devolviendo una lista de tuplas.
    silence_errors permite mostrar o no los errores.
    '''
    filas = csv.reader(nombre_archivo) # leemos el nombre_archivo que ya es un iterable
    if has_headers:
        # Lee los encabezados de nombre_archivo
        encabezados = next(filas)

            # Si se indicó un selector de columnas,
            # buscar los índices de las columnas especificadas.
            # Y en ese caso achicar el conjunto de encabezados para diccionarios

        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []
        contador= 0
        registros = []
        for fila in filas:
            contador += 1
            if not fila:    # Saltear filas vacías
                continue
            # Filtrar la fila si se especificaron columnas
            if indices:
                fila = [fila[index] for index in indices]
            try:
                if types:
                    fila = [func(val) for func, val in zip(types, fila) ]
            except ValueError as e:
                if silence_errors == False:
                    print(f'Fila {contador}: No pude convertir {fila}')
                    print(f'Fila {contador}: Motivo: {e}')
            # Armar el diccionario
            registro = dict(zip(encabezados, fila))
            registros.append(registro)
    else:
        if select: # lanzamos la excepcion si queremos seleccionar pero no definimos encabezados
            raise RuntimeError("Para seleccionar, necesito encabezados")
        registros = []
        for fila in filas:
            if not fila:    # Saltear filas vacías
                continue
            if types:
                fila = [val(func) for func, val in zip(fila, types)]
            # Armar la tupla
            registro = tuple(fila)
            registros.append(registro)
    return registros

# Retorna una lista de diccionarios [{'nombre', 'cajones', 'precio'}]
with open('../Data/camion.csv') as file: # mandamos un iterable a parse_csv
    camion = parse_csv(file, types=[str, int, float], has_headers=True, select=['nombre', 'cajones', 'precio'])
# Retorna una lista de tuplas [('nombre', precio)]
with open('../Data/precios.csv') as file:
    precios = parse_csv(file, types=[str, float], has_headers=False)