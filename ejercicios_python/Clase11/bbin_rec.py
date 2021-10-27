"""
Escribí una función recursiva bbinaria_rec(lista, e) que implemente la búsqueda binaria de un elemento e en una lista ordenada lista. La función debe devolver simplemente True o False indicando si el elemento está o no en la lista.
"""

def bbinaria_rec(lista, e):
    """
    Devuelve True o False si el elemento e está en la lista o no.
    """
    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = lista[0] == e
    else:
        medio = len(lista)//2
        if e >= lista[medio]:
            res = bbinaria_rec(lista[medio:], e)
        else:
            res = bbinaria_rec(lista[:medio], e)
    return res


lista_no = [1,3,4,5,6,8,9, 10, 11, 12, 13, 14, 15]
lista_si = [1,2,3,4,5,6,7,8,9, 10, 11, 12, 13, 14, 15]
print(bbinaria_rec(lista_no, 7))