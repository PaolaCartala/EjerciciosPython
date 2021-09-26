"""
Las columnas en camion.csv corresponden a un nombre de fruta, una cantidad de cajones cargados en el camión, y un precio de compra por cada cajón de ese grupo. Escribí un programa llamado costo_camion.py que abra el archivo, lea las líneas, y calcule el precio pagado por los cajones cargados en el camión.
- Modificá el programa para que atrape la excepción con un bloque try - except, imprima un mensaje de aviso (warning) y continúe procesando el resto del archivo.
- Modificá tu programa para que use el módulo csv para leer los archivos CSV.
"""
import csv

def costo_camion(nombre_archivo):
    """
    Esta función recibe un nombre de archivo como entrada, lee la información sobre los cajones que cargó el camión y devuelve el costo de la carga de frutas como una variable de punto flotante.
    """
    with open(nombre_archivo) as f:
        filas = csv.reader(f)
        header = next(filas)
        costo_total = 0
        for n_fila, fila in enumerate(filas, start=1):
                record = dict(zip(header, fila))
                try:
                    ncajones = int(record['cajones'])
                    precio = float(record['precio'])
                    costo_total += ncajones * precio
                except ValueError:
                    print(f"Fila {n_fila}: no pude interpretar {fila}")
        return costo_total
        
print(f"El costo total es ${costo_camion('../Data/camion.csv')}")