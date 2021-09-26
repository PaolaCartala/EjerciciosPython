"""
Copiá el contenido de costo_camion.py a un nuevo archivo llamado camion_commandline.py que incorpore la lectura de parámetros por línea de comando
"""
import csv
import sys

def costo_camion(nombre_archivo):
    """
    Esta función recibe un nombre de archivo como entrada desde la línea de comando, lee la información sobre los cajones que cargó el camión y devuelve el costo de la carga de frutas como una variable de punto flotante.
    """
    f = open(nombre_archivo)
    rows = csv.reader(f)
    header = next(rows)
    todos = []
    valido = True
    while valido:
        try:
            for row in rows:
                costo = float(row[-1])
                cantidad = float(row[1])
                todos.append(costo * cantidad)
                valido = False
            return sum(todos)
        except ValueError:
            valido = True
if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'

costo = costo_camion(nombre_archivo)
print(f"El costo total es ${costo}")