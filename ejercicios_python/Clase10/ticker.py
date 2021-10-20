"""
Comenzá creando una función que lea un archivo CSV.
- Escribí una función nueva que elija algunas columnas específicas.
- Escribí funciones generadoras que conviertan el tipo de datos a diccionarios.
- Para seguir agregando procesamiento a nuestro pipeline, escribí un filtro de datos que deje pasar únicamente aquellos lotes incluidos en el camión.
- Escribí una función ticker(camion_file, log_file, fmt) que cree un indicador en tiempo real para un camión, archivo log, y formato de tabla de salida particulares.
Modificá tu programa para que use expresiones generadoras en lugar de funciones generadoras.

Para utilizarlo, mantener corriendo el script "sim_mercado.py" generando datos, descomentar la útlima línea de llamado de la función y correr este archivo.
Para ejecutarlo en el intérprete de Python (tambien con "sim_mercado.py" corriendo):
> from ticker import ticker
> ticker('../Data/camion.csv', '../Data/mercadolog.csv', 'txt') Imprime la tabla en formato txt.
> ticker('../Data/camion.csv', '../Data/mercadolog.csv', 'csv') Lo mismo en formato csv.
> ticker('../Data/camion.csv', '../Data/mercadolog.csv', 'html') Lo mismo en formato html.
"""

#%%
from vigilante import vigilar
import csv
import formato_tabla
import informe_final

#%%
def elegir_columnas(rows, indices):
    """
    Elije columnas específicas
    """
    return ([row[index] for index in indices] for row in rows)

def cambiar_tipo(rows, types):
    """
    Genera datos de tipos específicos
    """
    return ([func(val) for func, val in zip(types, row)] for row in rows)

def hace_dicts(rows, headers):
    """
    Genera diccionarios con los headers y rows
    """
    return (dict(zip(headers, row)) for row in rows)

def parsear_datos(lines):
    """
    Lee un archivo CSV y devuelve diccionario
    """
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, int])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows

def filtrar_datos(rows, nombres):
    """
    Filtra los datos
    """
    return (row for row in rows if row['nombre'] in nombres)

def ticker(camion_file, log_file, fmt):
    """
    Imprime una tabla con formato fmt que contiene los datos de log_file filtrados por camion_file
    """
    camion = informe_final.leer_camion(camion_file)
    lines = vigilar(log_file)
    rows = parsear_datos(lines)
    filas = filtrar_datos(rows, camion)
    cols = ['nombre', 'precio', 'volumen']
    formateador = formato_tabla.crear_formateador(fmt)
    formateador.encabezado(cols)
    for row in filas:
        formateador.fila([str(row[cols[0]]), str(row[cols[1]]), str(row[cols[2]])])

#%%
ticker('../Data/camion.csv', '../Data/mercadolog.csv', 'txt')
