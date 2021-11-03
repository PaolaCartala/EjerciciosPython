"""
El ordenamiento por burbujeo se basa en una idea bastante sencilla. El algoritmo compara dos elementos contiguos de la lista y, si el orden es adecuado, los deja como están, si no, los intercambia.
Programá una función ord_burbujeo(lista) que implemente este método de ordenamiento. Debe tomar una lista y devolver la lista ordenada. ¿Cuántas comparaciones realiza esta función en una lista de largo n?
"""

def ord_burbujeo(lista):
    """
    Compara dos elementos contiguos de lista, si el orden es adecuado los deja como están, sino los intercambia. Devuelve la lista ordenada. Imprime la cantidad de comparaciones que realiza en el proceso.
    """
    contador = 0
    for _ in range(len(lista)):
        for i in range(len(lista) - 1):
            if lista[i + 1] < lista[i]:
                v = lista[i + 1]
                j = i + 1
                lista[j] = lista[j - 1]
                j -= 1
                lista[j] = v
                contador += 1
                print("DEBUG: ", contador, lista)
    return lista

lista = [9,8,7,6,5,4,3,2,1]
lista_1 = [1, 2, -3, 8, 1, 5]
lista_2 = [1, 2, 3, 4, 5]
lista_3 = [0, 9, 3, 8, 5, 3, 2, 4]
lista_4 = [10, 8, 6, 2, -2, -5]
lista_5 = [2, 5, 1, 0]
print(ord_burbujeo(lista_5))