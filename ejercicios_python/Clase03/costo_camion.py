"""
Las columnas en camion.csv corresponden a un nombre de fruta, una cantidad de cajones cargados en el camión, y un precio de compra por cada cajón de ese grupo. Escribí un programa llamado costo_camion.py que abra el archivo, lea las líneas, y calcule el precio pagado por los cajones cargados en el camión.
El archivo ..Data/missing.csv contiene datos sobre los cajones de un camión, pero tiene algunas filas que faltan. Usando enumerate(), copiá tu programa costo_camion.py a la carpeta de la clase actual, y modificalo de forma que imprima un aviso (warning) cada vez que encuentre una fila incorrecta, indicando el número de fila.
Tratá de aparear los encabezados con una fila de datos para que entienda que la columna tiene el precio por su encabezado y no por su posición dentro del archivo.
"""
import csv

def costo_camion(nombre_archivo):
    """
    Esta función recibe un nombre de archivo como entrada, lee la información sobre los cajones que cargó el camión y devuelve el costo de la carga de frutas como una variable de punto flotante. En caso de faltar algún dato en la fila, imprime el número de fila y la lista con el dato que no se pudo interpretar.
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
        
print(f"El costo total con datos faltantes es ${costo_camion('../Data/missing.csv')}")
print(f"El costo total con datos apareados es ${costo_camion('../Data/fecha_camion.csv')}")