"""
En este primer ejercicio tenés que escribir una función buscar_u_elemento() que reciba una lista y un elemento y devuelva la posición de la última aparición de ese elemento en la lista (o -1 si el elemento no pertenece a la lista).
Agregale a tu programa una función buscar_n_elemento() que reciba una lista y un elemento y devuelva la cantidad de veces que aparece el elemento en la lista. Probá también esta función con algunos ejemplos.
Agregale a tu archivo una función maximo() que busque el valor máximo de una lista de números positivos, luego otra función minimo()
"""

def buscar_u_elemento(lista, elemento):
    """
    Recibe como argumentos un elemento y lo busca en la lista, devuelve la posición en caso de estar en la lista y si no está devuelve -1
    """
    posicion = 0
    if elemento not in lista:
        return -1
    for n, i in enumerate(lista):
        if elemento == i:
            posicion = n
    return posicion

print(buscar_u_elemento([1, 2, 3, 2, 3, 4], 3))

def buscar_n_elemento(lista, elemento):
    """
    Recibe como argumentos una lista y busca la cantidad de veces que está el elemento presente
    """
    cantidad = 0
    for i in lista:
        if i == elemento:
            cantidad += 1
    return cantidad

print(buscar_n_elemento([1, 2, 3, 2, 3, 4], 2))

def maximo(lista):
    """
    Busca el valor máximo de la lista
    """
    m = 0
    for e in lista:
        if e > m:
            m = e
    return m

print(maximo([5, 4]))

def minimo(lista):
    """
    Busca el valor mínimo de la lista
    Pre: la lista debe tener números menores a 100
    """
    m = 100
    for e in lista:
        if e < m:
            m = e
    return m

print(minimo([5, -15]))