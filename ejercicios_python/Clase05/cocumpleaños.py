"""
Haciendo miles de experimentos numéricos, estimá la probabilidad de que en un grupo de 30 personas elegidas al azar, dos cumplan años el mismo día. Escribí un programita que permita calcular esa probabilidad asumiendo que el año tiene 365 días.
"""

import random

def cocumpleaños(n):
    cumpleaños = []
    repetidos = 0
    for _ in range(n):
        for _ in range(30):
            cumpleaños.append(random.randint(1, 365))
        for i in cumpleaños:
            numero = cumpleaños.count(i)
            if numero > 2:
                cumpleaños.remove(i)
                repetidos += 1
    probabilidad = repetidos / (n * 30)
    return probabilidad

print(cocumpleaños(1000))