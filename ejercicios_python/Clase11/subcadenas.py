"""
Escribí una funcion recursiva posiciones(a, b) que reciba como parámetros dos cadenas a y b, y devuelva una lista con las posiciones en donde se encuentra b dentro de a.
"""

def posiciones(a, b):
    """
    Devuelve una lista con las posiciones donde b está en a.
    """
    lista = []
    if len(b) > len(a):
        return []
    for n, l in enumerate(a.lower()):
        try:
            if a[n]+a[n+1] == b:
                lista.append(n)
            else:
                posiciones(a[n+1], b)
        except IndexError:
            continue
    return lista


print(posiciones('Un tete a tete con Tete', 'te'))
