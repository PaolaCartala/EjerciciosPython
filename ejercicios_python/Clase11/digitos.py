"""
Escribí una función recursiva cant_digitos(n) que reciba un número positivo, n, y devuelva la cantidad de dígitos que tiene.
"""

def cant_digitos(n):
    """
    Devuelve la cantidad de dígitos para cualquier número entero, excepto 0.
    """
    n = abs(n)
    if n == 0:
        return 0
    return 1 + cant_digitos(n // 10) 
        

print(cant_digitos(100))