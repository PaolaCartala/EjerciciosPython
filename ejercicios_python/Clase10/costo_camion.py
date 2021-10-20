#! python3

"""
Cambiá el código en costo_camion() para que use objetos que sean instancias de la clase Camion.
Para ejecutarlo en el símbolo del sistema (Windows) tenes que posicionarte en la carpeta Clase10 y correr la línea:
> python costo_camion.py ../Data/camion.csv
Para ejecutarlo en el intérprete de Python:
> import costo_camion
> costo_camion.costo_camion('../Data/camion.csv')
"""

from informe_final import leer_camion
import sys

def costo_camion(nombre_archivo):
    """
    Devuelve el costo total del camion
    """
    camion = leer_camion(nombre_archivo)
    return camion.precio_total()

def f_principal(argv):
    costo = costo_camion(argv[1]) 
    print(f'Costo total: ${costo}')

if __name__ == '__main__':
    import sys
    f_principal(sys.argv)