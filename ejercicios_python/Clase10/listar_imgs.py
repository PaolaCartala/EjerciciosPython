#! python3

"""
Usá los datos que te proporciona os.walk y una expresión generadora para filtrar las imágenes png (con sus directorios correspondientes). Este filtro debería generar pares (directorio, archivo.png).

Ejecución desde la línea de comandos:
Extraer el archivo ordenar.zip de la carpeta Data en esa misma carpeta.
> python listar_imgs.py ../Data/ordenar
"""

import os

#%%
for root, dirs, files in os.walk('../Data/ordenar'):
    name = (name for name in files if name[-4:] == '.png')
    for archivo in name:
        print((root, archivo))
