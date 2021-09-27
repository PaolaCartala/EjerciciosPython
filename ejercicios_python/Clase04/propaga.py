"""
Imaginate una fila con varios fósforos uno al lado del otro. Los fósforos pueden estar en tres estados: nuevos, prendidos fuego o ya gastados (carbonizados). Representaremos esta situación con una lista con un elemento por fósforo, que en cada posición tiene un 0 (nuevo), un 1 (encendido) o un -1 (carbonizado). El fuego se propaga inmediatamente de un fósforo encendido a cualquier fósforo nuevo que tenga a su lado. Los fósforos carbonizados no se encienden nuevamente.
Escribí una función llamada propagar que reciba un vector con 0's, 1's y -1's y devuelva un vector en el que los 1's se propagaron a sus vecinos con 0.
"""

def propagar(lista):
    """
    Recibe una lista con 0, 1 y -1 de los cuales los 0 se vuelven 1 al estar al lado de otro 1. Los -1 no cambian su estado.
    Pre: los números de la lista solo pueden ser 0, 1 y -1.
    """
    lista_propagada = [0] * len(lista)
    for i, n in enumerate(lista):
        if i == 0:
            lista_propagada[i] = n
        if n == 0:
            if lista_propagada[i-1] == 1:
                lista_propagada[i] = 1
            else:    
                lista_propagada[i] = n
        else:
            lista_propagada[i] = n
    for e in range(len(lista_propagada)-1,-1,-1):
        if lista_propagada[e] == 0:
            if lista_propagada[e + 1] == 1:
                lista_propagada[e] = 1
    return lista_propagada

print(propagar([0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]))