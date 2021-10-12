#! python3

"""
Definí una función llamada archivos_png(directorio) que arme una lista de todos los archivos .png que se encuentren en algún subdirectorio directorio dado. Tu programa debe poder ejecutarse desde la línea de comandos recibiendo como parámetro el directorio a leer original.
Ejecución desde la línea de comandos:
> python listar_imgs.py ../Data/ordenar
"""

import os
import sys

def archivos_png(directorio):
    """
    Recorre el directorio y guarda los archivos .png en una lista y la devuelve
    """
    png = []
    for root, dirs, files in os.walk(directorio):
        for name in files:
            if name[-4:] == '.png':
                png.append(name)
    return png

if __name__ == '__main__':
    print(archivos_png(sys.argv[1]))
