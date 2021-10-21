'''
Seguimos aquí con el arbolado porteño.
- Basándote en la función leer_parque(nombre_archivo, parque), escribí otra leer_arboles(nombre_archivo) que lea el archivo indicado y devuelva una lista de diccionarios con la información de todos los árboles en el archivo. La función debe devolver una lista conteniendo un diccionario por cada árbol con todos los datos. Vamos a llamar arboleda a esta lista.
- Usando comprensión de listas y la variable arboleda podés por ejemplo armar la lista de la altura de los árboles. Usá los filtros para armar la lista de alturas de los Jacarandás solamente.
- Ahora te proponemos que armes una nueva lista que tenga pares (tuplas de longitud 2) conteniendo no solo el alto sino también el diámetro de cada Jacarandá en la lista.
- Te pedimos que armes un diccionario en el que otras especies sean las claves y los valores asociados sean los datos que generaste en el ejercicio anterior. Más aún, organizá tu código dentro de una función medidas_de_especies(especies,arboleda) que recibe una lista de nombres de especies y una lista y devuelve un diccionario cuyas claves son estas especies y sus valores asociados sean las medidas generadas en el ejercicio anterior. Extra: casi todes usan un for para crear este diccionario, intentá hacerlo usando una comprensión de diccionarios
'''

import csv

def leer_arboles(nombre_archivo):
    """
    Devuelve una lista de diccionarios con TODOS los arboles del archivo
    """
    f = open(nombre_archivo, encoding="utf8")
    rows = csv.reader(f)
    header = next(rows)
    arboleda = []
    for n_row, row in enumerate(rows, start=1):
        fuente = dict(zip(header, row))
        arboleda.append(fuente)
    return arboleda

arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')

# Lista de altos de jacaranda
# devuelve las alturas de los arboles si son jacaranda
h = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']

# Lista de altos y diametros de jacaranda
# devuelve una tupla con los valores de altura y diametro de los jacaranda
j = [tuple((float(arbol['altura_tot']), int(arbol['diametro']))) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá'] 

# Diccionario con medidas
def medidas_de_especies(especies, arboleda):
    """
    Devuelve un diccionario con cada {especie: [(altura, diametro)]}
    """
    diccionario = { especie: [tuple((float(arbol['altura_tot']), int(arbol['diametro']))) for arbol in arboleda if arbol['nombre_com'] == especie] for especie in especies }
    return diccionario

medidas_de_especies(['Eucalipto', 'Palo borracho rosado', 'Jacarandá'], arboleda)