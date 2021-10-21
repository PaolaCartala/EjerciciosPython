"""
Escribí un programa estimar_pi.py que genere cien mil puntos aleatorios con la función generar_punto(), calcule la proporción de estos puntos que caen en el círculo unitario (usando ¿x^2 + y^2 < 1?) y use este resultado para dar una aproximación de pi.
"""

import random

def generar_punto():
    x = random.random()
    y = random.random()
    return x,y

n = 100000
m = 0
for i in range(n):
    x, y = generar_punto()
    if x**2 + y**2 < 1:
        m += 1
print(f'pi ~ {4*m/n:.5f}')