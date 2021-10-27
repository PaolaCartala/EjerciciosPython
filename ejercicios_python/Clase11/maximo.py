"""
Escribí una funcion recursiva maximo(lista) que encuentre y devuelva el mayor elemento de una lista (sin usar max()).
"""

def maximo(lista, maxi = 0):
    """
    Devuelve el mayor número de la lista
    """
    res = maxi
    if len(lista) > 1:
        if maxi < lista[-1]:
            maxi = lista.pop()
            res = maximo(lista, maxi)
        else:
            lista.pop()
            res = maximo(lista, maxi)
    return res

lista = [1, 50, 8, 15, 500, 150, 300, 800]
print(maximo(lista))