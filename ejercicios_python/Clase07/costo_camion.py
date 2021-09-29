#! python3

"""
Modificá tu programa costo_camion.py para que pueda ser ejecutado como script desde la línea de comandos.

Para ejecutarlo en el símbolo del sistema (Windows) tenes que posicionarte en la carpeta Clase07 y correr la línea
> python costo_camion.py ../Data/camion.csv
"""

from informe_final import leer_camion
import sys

def costo_camion(nombre_archivo):
    """
    Devuelve el costo total del camion
    """
    camion = leer_camion(nombre_archivo)
    costo_total = 0
    for item in camion:
        costo_total += item['cajones'] * item['precio']
    return costo_total
        
if __name__ == '__main__':
    print(f'Costo total: ${costo_camion(sys.argv[1])}')