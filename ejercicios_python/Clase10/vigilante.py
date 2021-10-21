"""
Modificá el código de modo que la lectura del archivo esté resuelta por una única función generadora vigilar() a la que se le pasa un nombre de archivo como parámetro.
Modificá el programa para que sólo informe las líneas que tienen precios de lotes incluídos en un camión, e ignore el resto de los productos.

Para utilizarlo, mantener corriendo el script "sim_mercado.py" generando datos y correr este archivo.
"""

import os
import time

def vigilar(archivo):
    f = open(archivo)
    f.seek(0, os.SEEK_END)
    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.5)
            continue
        yield line

if __name__ == '__main__':
    import informe_final

    camion = informe_final.leer_camion ('../Data/camion.csv')

    for line in vigilar('../Data/mercadolog.csv'):  
        fields = line.split(',')
        nombre = fields[0].strip('"')
        precio = float(fields[1])
        volumen = int(fields[2])

        if nombre in camion:    
            print(f'{nombre:>10s} {precio:>10.2f} {volumen:>10d}')
