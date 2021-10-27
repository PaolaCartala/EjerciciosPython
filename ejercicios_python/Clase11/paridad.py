"""
Escribí dos funciones mutualmente recursivas par(n) e impar(n) que determinen la paridad del numero natural dado.
"""

def impar(n):
    """
    Devuelve True si n es impar.
    :pre: n > 0
    """
    while n >= 1:
        if n == 1:
            return True
        else:
            return impar(n - 2)
    return False

def par(n):
    """
    Devuelve True si n es par.
    :pre: n > 0
    """
    while n > 1:
        if impar(n + 1) == True:
            return True
        else:
            return par(n - 2)
    return False

print(par(4))