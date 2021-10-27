"""
Escribí una función triangular(n) que calcule recursivamente el n-ésimo número triangular (es decir, el número 1 + 2 + 3 + ... + n).
"""

def triangular(n):
    """
    Devuelve la suma triangular de cualquier entero mayor a 0
    """
    if n == 1:
        return 1
    else:
        return n + triangular(n - 1)

print(triangular(10))