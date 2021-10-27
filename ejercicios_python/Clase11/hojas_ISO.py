"""
Escribí una función recursiva medidas_hoja_A(N) que para una entrada N mayor que cero, devuelva el ancho y el largo de la hoja A(N). La función debe devolver el ancho y el largo -en ese orden- en una tupla.
"""

def medidas_hoja_A(n):
    """
    Devuelve la medida en mm del ancho y el largo de una hoja A(n) siendo n la medida estándar de las hojas desde A0 hasta A10.
    """
    if n == 0:
        return (841, 1189)
    else:
        return (medidas_hoja_A(n - 1)[1] // 2, medidas_hoja_A(n - 1)[0])

print(medidas_hoja_A(9))