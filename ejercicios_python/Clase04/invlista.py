"""
Escribí una función invertir_lista(lista) que dada una lista devuelva otra que tenga los mismos elementos pero en el orden inverso. Es decir, el que era el primer elemento de la lista de entrada deberá ser el último de la lista de salida y análogamente con los demás elementos.
"""

def invertir_lista(lista):
    """
    Invierte la lista pasada como argumento
    """
    invertida = []
    for n, e in enumerate(lista):
        invertida.insert(-n, e)
    print(invertida)

invertir_lista([1, 2, 3, 4, 5])
invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel'])
