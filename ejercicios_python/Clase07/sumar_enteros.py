"""
En este ejercicio vas a realizar dos implementaciones correspondientes a la función sumar_enteros.
En la primera implementación te pedimos que uses un ciclo.
En la segunda te pedimos que lo hagas sin ciclos: implementá la función de manera que trabaje en tiempo constante (es decir, usando una cantidad de operaciones que no depende de las entradas a la función.
Ayuda: Estas sumas se pueden escribir como diferencia de dos números triangulares.
"""

def sumar_enteros(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    Inv: suma siempre será mayor que en la iteración anterior
    '''
    suma = 0
    if hasta > desde:
        for i in range(desde, hasta + 1):
            suma += i
    else:
        suma = 0
    return suma

print(f'Con ciclo: {sumar_enteros(10, 20)}')

def sumar_enteros_triangular(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    Inv: suma siempre será mayor que en la iteración anterior
    '''
    if hasta > desde:
        desde_triangular = desde * (1 + desde) // 2
        hasta_triangular = hasta * (1 + hasta) // 2
        suma = hasta_triangular - desde_triangular + desde
    else:
        suma = 0
    return suma

print(f'Con triangulares: {sumar_enteros_triangular(10, 20)}')