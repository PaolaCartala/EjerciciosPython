"""
Escribi un programa que le pida a le usuarie que ingrese por teclado el radio r de una esfera y calcule e imprima el volumen de la misma. Sugerencia: recordar que el volumen de una esfera es 4/3 πr^3.

Finalmente, responde ¿cuál es el volumen de una esfera de radio 6?
"""

import math
radio = int(input("Ingrese el radio de la esfera que quiere calcular: \n"))
volumen = 4/3 * math.pi * radio ** 3
print(f"El volúmen de la esfera es de: {volumen}")