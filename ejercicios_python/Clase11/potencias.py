"""
Escribí una función recursiva es_potencia(n, b) que reciba 2 enteros, n y b, y devuelva True si n es potencia de b y False en caso contrario.
"""
#%%
def es_potencia(n, b):
    """
    Verifica si el número n es potencia del número b
    :pre: ambos números son mayores que 0.
    """
    e = 0
    def es_potencia_aux(n, b, e):
        while b ** e <= n:
            if (b ** e) == n:
                return n
            else:
                e += 1
                es_potencia_aux(n, b, e)
    if es_potencia_aux(n, b, e) == n:
        return True
    else:
        return False

#%%
print(es_potencia(8, 2))
print(es_potencia(64, 4))
print(es_potencia(70, 10))
print(es_potencia(1, 2))