"""
Construí una función que, a partir de una lista de palabras, devuelva un diccionario geringoso.
"""

def diccionario_geringoso(lista):
    """
    Itera la lista pasada por parámetro de modo que cada letra de cada palabra sea evaluada y en caso de ser una vocal sea reemplazada por apa, epe, ipi, opo, upu según corresponda, luego arma un diccionario con cada palabra como clave y su equivalente en geringoso como valor.
    """
    d = {}
    for i in lista:
        values = ''
        for c in i:
            if c == "a":
                values = values + "apa"
            elif c == "e":
                values = values + "epe"
            elif c == "i":
                values = values + "ipi"
            elif c == "o":
                values = values + "opo"
            elif c == "u":
                values = values + "upu"
            else: values = values + c
        d[i] = values
    return d

diccionario_geringoso(['banana', 'manzana', 'mandarina'])