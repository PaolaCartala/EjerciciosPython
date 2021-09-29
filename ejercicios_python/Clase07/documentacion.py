"""
Para cada una de las siguientes funciones: * Pensá cuál es el contrato de la función. * Agregale la documentación adecuada. * Comentá el código si te parece que aporta. * Detectá si hay invariantes de ciclo y comentalo al final de la función.
"""

def valor_absoluto(n):
    """
    Devuelve el valor absoluto de un número n
    Pre: n debe ser un número
    Pos: devolverá el valor absoluto de n
    """
    if n >= 0:
        return n
    else:
        return -n

# Inv: n absoluto

def suma_pares(l):
    """
    Suma todos los números pares de la lista l
    Pre: l debe ser una lista que contenga números
    Pos: devuelve la suma de los números pares de la lista l
    """
    res = 0
    for e in l:
        if e % 2 == 0:
            res += e
        else:
            res += 0

    return res

# Inv: res es par

def veces(a, b):
    """
    Devuelve el resultado de a * b
    Pre: a y b deben ser números enteros
    Pos: devuelve un entero resultado de la operación
    """
    res = 0
    nb = b
    while nb != 0:
        # print(nb * a + res)
        res += a
        nb -= 1
    return res

# Inv: res es la diferencia de nb * a - b * a

def collatz(n):
    """
    Si el numero n es par, lo divide por 2 y si el numero es impar lo multiplica por 3 y le suma 1, cuenta la cantidad de veces que debe hacer esta operacion para reducirlo a 1.
    Pre: n debe ser un numero entero
    Pos: devuelve la cantidad de operaciones que se realizaron
    """
    res = 1
    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res

# Inv: res es mayor a 1

print(f'collatz = {collatz(17)}')