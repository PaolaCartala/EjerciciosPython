"""
Escribí una función recursiva replicar(lista, n) para replicar los elementos de una lista una cantidad n de veces.
"""

def replicar(lista, cantidad):
    """
    Replica los elementos de la lista n cantidad de veces y los devuelve ordenados
    """
    if cantidad > 1:
        lista += lista
        lista.sort()
        return replicar(lista, cantidad - 1)
    return lista

lista = [1, 3, 3, 7]
print(replicar(lista, 2))