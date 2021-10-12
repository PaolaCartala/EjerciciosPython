#! python3

"""
CUIDADO: Este script MODIFICA y ELIMINA archivos de manera permanente.
Escribí un programa que te permita ordenar las imágenes PNG de esta carpeta.
- Al final, tu script debería poder ejecutarse desde la línea de comandos recibiendo como parámetro el directorio a leer original y un directorio destino (que debería ser creado si no existe).
- Te pedimos que modularices el procesamiento de los archivos png.
- Usá docstrings y comentarios en tu código de manera que sea legible.
- Al terminar de usar el código, comentá todas las instrucciones salvo los imports y las definiciones de funciones.
Modo de uso:
- Extrear el archivo ordenar.zip en /Data
- Correr el script UNA VEZ
- En caso de querer probar nuevamente el script, eliminar /Data/ordenar y /Data/img_procesadas y volver a extraer ordenar.zip
"""

import os, sys
from datetime import datetime
import shutil

def procesar_nombre(fname):
    if fname[-4:] == '.png': # verificamos si termina en png
        os.chdir(root) # cambio el directorio para que busque los archivos
        if fname[-12:-4].isdigit():
            fecha = datetime(int(fname[-12:-8]), int(fname[-8:-6]), int(fname[-6:-4])) # pasamos a datetime los caracteres del nombre
            # print(fname[-12:-4])
            os.rename(fname, fname[:-13]+'.png') # renombramos el archivo
            return (fname[:-13]+'.png', fecha)
        else:
            return fname
    else:
        return fname

def procesar(fname, destino):
    os.chdir(os.path.dirname(os.path.abspath(__file__))) # cambiamos el directorio donde está trabajando windows a la carpeta actual del script
    if not os.path.exists(destino): # verificamos si existe la carpeta img_procesadas y si no, la creamos
        os.mkdir(destino) # '../Data/imgs_procesadas/'
    timestamp = fname[1].timestamp() # pasamos la fecha a timestamp
    os.utime(os.path.join(root, fname[0]), (timestamp, timestamp)) # utime setea la fecha de acceso y modificacion, el primer parámetro es el path del archivo, el segundo es una tupla con el timestamp de atime (acceso) y mtime (modificación) que queremos setear
    if (fname[0])[-4:] == '.png':
        shutil.move(os.path.join(root, fname[0]), destino)

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__))) # cambiamos el directorio donde está trabajando windows a la carpeta actual del script
    os.chdir(sys.argv[1]) # cambiamos el directorio donde está trabajando windows al pasado por parámetro
    for root, dirs, files in os.walk(os.getcwd()): # recorremos el directorio
        for name in files:
            archivo = procesar_nombre(name)
            if name[-4:] == '.png':
                # funcion de procesarlo
                archivo_procesado = procesar(archivo, sys.argv[2])
    os.chdir(sys.argv[1])
    for root, dirs, files in os.walk(os.getcwd()):
        for name in dirs:
            if os.listdir(os.path.join(root, name)) == []:
                os.rmdir(os.path.join(root, name))