"""
Definí una función donde_insertar(lista, x) de forma que reciba una lista ordenada y un elemento y devuelva la posición de ese elemento en la lista (si se encuentra en la lista) o la posición donde se podría insertar el elemento para que la lista permanezca ordenada (si no está en la lista).
Agrega una función insertar(lista, x) que reciba una lista ordenada y un elemento. Si el elemento se encuentra en la lista solamente devuelve su posición; si no se encuentra en la lista, lo inserta en la posición correcta para mantener el orden. En este segundo caso, también debe devolver su posición.
"""

def donde_insertar(lista, x):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve p tal que lista[p] == x, si x está en lista
    Devuelve la posición de x si no está en la lista original insertándolo previamente de manera que ésta permanezca ordenada
    '''
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    if pos == -1: # si al finalizar la busqueda x no esta en la lista
        lista.insert(izq, x) # insertamos x
        pos = izq # devolvemos su posición en la lista
    return pos

print(donde_insertar([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23],11))

def insertar(lista, x):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve p tal que lista[p] == x, si x está en lista
    Devuelve la posición de x si no está en la lista original insertándolo previamente de manera que ésta permanezca ordenada
    '''
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    if pos == -1: # si al finalizar la busqueda x no esta en la lista
        lista.insert(izq, x) # insertamos x
        pos = izq # devolvemos su posición en la lista
    return pos

print(insertar([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23],17))