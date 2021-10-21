"""
Escribí un programa tablamult.py que imprima de forma prolija las tablas de multiplicar del 1 al 9 usando f-strings.
"""

multiplo = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
tabla = {}
for i in range(10):
    multiplicacion = []
    for m in multiplo:
        multiplicacion.append(m * i)
        tabla[i] = multiplicacion

header = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(f'{header[0]:>6d} {header[1]:>4d} {header[2]:>4d} {header[3]:>4d} {header[4]:>4d} {header[5]:>4d} {header[6]:>4d} {header[7]:>4d} {header[8]:>4d} {header[9]:>4d}')
print(f'{"-"*53}')
for n, t in enumerate(tabla):
    print(f'{n}: {tabla[t][0]:>3d} {tabla[t][1]:>4d} {tabla[t][2]:>4d} {tabla[t][3]:>4d} {tabla[t][4]:>4d} {tabla[t][5]:>4d} {tabla[t][6]:>4d} {tabla[t][7]:>4d} {tabla[t][8]:>4d} {tabla[t][9]:>4d}')

