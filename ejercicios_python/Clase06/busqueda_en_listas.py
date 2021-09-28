"""
Modificá la función busqueda_lineal(lista, e) para el caso de listas ordenadas, de forma que la función pare cuando encuentre un elemento mayor a e.
La función busqueda_binaria(lista, x, verbose=False) muestra una implementación del algoritmo de búsqueda binaria, incluyendo una instrucción de depuración(debug) con print para verificar su funcionamiento.
- Modificá el código de búsqueda binaria de forma que devuelva (además de la posición del elemento en la lista) la cantidad de comparaciones que realizó el algoritmo para encontrarlo o decidir que no está.
La siguiente función generar_lista(n, m) devuelve una lista ordenada de n elementos diferentes entre 0 y m-1, mientras que generar_elemento(m) devuelve un elemento aleatorio en el mismo rango de valores. Un experimento elemental es generar un elemento, buscarlo en la lista y contar la cantidad de comparaciones realizadas. Esta cantidad de operaciones es el resultado del experimento elemental.
"""

import random

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

buscar_u_elemento([1, 2, 3, 2, 3, 4], 3)

def buscar_n_elemento(lista, elemento):
    """
    Recibe como argumentos una lista y busca la cantidad de veces que está el elemento presente
    """
    cantidad = 0
    for i in lista:
        if i == elemento:
            cantidad += 1
    return cantidad

buscar_n_elemento([1, 2, 3, 2, 3, 4], 2)

def maximo(lista):
    """
    Busca el valor máximo de la lista
    """
    m = 0
    for e in lista:
        if e > m:
            m = e
    return m

maximo([-5, -4])

def minimo(lista):
    """
    Busca el valor mínimo de la lista
    Pre: la lista debe tener números menores a 100
    """
    m = 0
    for e in lista:
        if e < m:
            m = e
    return m

minimo([-5, -4])

def busqueda_lineal(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    lista.sort()
    pos = -1
    for i, z in enumerate(lista): # recorremos la lista
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
    return pos

def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    También cuenta las comparaciones que realiza
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    comparaciones = 0
    while izq <= der:
        comparaciones += 1
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos, comparaciones

# print(busqueda_lineal([1, 4, 54, 3, 0, -1], 0))
# busqueda_binaria([1, 3, 5], 1, verbose = True)
# busqueda_binaria([1, 3, 5], 3, verbose = True)
# busqueda_binaria([1], 1, verbose = True)

def busqueda_secuencial_(lista, x):
    '''Si x está en la lista devuelve el índice de su primera aparición, 
    de lo contrario devuelve -1. Además devuelve la cantidad de comparaciones
    que hace la función.
    '''
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 # sumo la comparación que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps

# print(f'Binaria: {busqueda_binaria([1, 3, 5], 0, verbose = True)[1]}')
# print(f'Secuencial: {busqueda_secuencial_([1, 3, 5], 0)[1]}')
# print(f'Binaria: {busqueda_binaria([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23],18, verbose = False)[1]}')
# print(f'Secuencial: {busqueda_secuencial_([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23],18)[1]}')

def generar_lista(n, m):
    """
    Devuelve una lista ordenada de n elementos diferentes entre 0 y m-1
    """
    l = random.sample(range(m), k = n)
    l.sort()
    return l

def generar_elemento(m):
    """
    Devuelve un elemento aleatorio en el mismo rango de valores
    """
    return random.randint(0, m-1)

m = 10000
n = 100
lista = generar_lista(n, m)

# Acá comienza el experimento
# Experimento elemental (generar un elemento, buscarlo en la lista y contar la cantidad de comparaciones realizadas)
x = generar_elemento(m)
# Resultado (cantidad de comparaciones)
comps = busqueda_secuencial_(lista, x)[1]
# print(f'Comparaciones: {comps}')