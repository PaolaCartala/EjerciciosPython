#! python3

"""
Cambiá un poco el código en informe_final.py y en costo_camion.py de modo que funcionen con objetos Lote (instancias de la clase Lote) en lugar de diccionarios.
Para ejecutarlo en el símbolo del sistema (Windows) tenes que posicionarte en la carpeta Clase09 y correr la línea
> python costo_camion.py ../Data/camion.csv
"""

from informe_final import leer_camion
import sys

def costo_camion(nombre_archivo):
    """
    Devuelve el costo total del camion
    """
    camion = leer_camion(nombre_archivo)
    costo_total = sum([c.costo() for c in camion])
    return costo_total

def f_principal(argv):
    costo = costo_camion(argv[1]) 
    print(f'Costo total: ${costo}')

if __name__ == '__main__':
    import sys
    f_principal(sys.argv)