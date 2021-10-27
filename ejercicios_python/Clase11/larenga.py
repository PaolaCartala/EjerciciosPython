"""
El triángulo de Pascal es un arreglo triangular de números que se define de la siguiente manera: Las filas se enumeran desde n = 0, de arriba hacia abajo. Los valores de cada fila se enumeran desde k = 0 (de izquierda a derecha). Los valores que se encuentran en los bordes del triángulo son todos unos. Cualquier otro valor se calcula sumando los dos valores contiguos de la fila de arriba.
Escribí la función recursiva pascal(n, k) que calcula el valor que se encuentra en la fila n y la columna k.
"""

def pascal(n, k):
    """
    Calcula el valor de la fila n y columna k en un triangulo de Pascal.
    """
    def triangulo(filas):
        fila = [1]
        cero = [0]
        for i in range(filas):
            fila = [i + d for i, d in zip(fila + cero, cero + fila)]
        return fila
    fila = triangulo(n)
    if n == 0 or k == 0:
        res = 1
    else:
        pascal(n - 1, k - 1)
        res = fila[k]
    return res

print(pascal(5, 2))