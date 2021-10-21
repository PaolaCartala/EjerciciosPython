"""
Hagamos una lista de Python con los nombres de las funciones de conversión que necesitamos para convertir cada columna al tipo apropiado, hagamos un Zip de la lista de tipos con la de datos y veamos el resultado.
Hagamos un diccionario usando el encabezado de las columnas.
Usando las técnicas de este ejercicio, vas a poder escribir instrucciones que conviertan fácilmente campos como los de nuestro archivo en un diccionario de Python. Bonus: ¿Cómo modificarías este ejemplo para transformar la fecha (date) en una tupla como (6, 11, 2007)?
"""

import csv

# Datos de primera clase
# lista con funciones
types = [str, int, float]
f = open('../Data/camion.csv')
rows = csv.reader(f)
headers = next(rows)
# lista con datos
row = next(rows)

print(row) # ['Lima', '100', '32.2']
print(types[1]) # <class 'int'>
print(row[1]) # 100
print(types[1](row[1]) * types[2](row[2])) # 3220.0000000000005

r = list(zip(types, row))
print(r) # [(<class 'str'>, 'Lima'), (<class 'int'>, '100'), (<class 'float'>, '32.2')]

# Usando zip podemos asignar los valores a las funciones (convirtiendolos) y agregarlos a una lista
# converted = []
# for func, val in zip(types, row):
#     converted.append(func(val))

# Y tambien lo podemos hacer en una sola linea con comprension de listas
converted = [func(val) for func, val in zip(types, row)]
print(converted) # ['Lima', 100, 32.2]

#  Diccionarios
print(dict(zip(headers, converted))) # {'nombre': 'Lima', 'cajones': 100, 'precio': 32.2}

# lo mismo con comprension de diccionarios
print({name: func(val) for name, func, val in zip(headers, types, row)}) # {'nombre': 'Lima', 'cajones': 100, 'precio': 32.2}

# Fijando ideas
f = open('../Data/dowstocks.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)
print(headers) # ['name', 'price', 'date', 'time', 'change', 'open', 'high', 'low', 'volume']
print(row) # ['AA', '39.48', '6/11/2007', '9:36am', '-0.18', '39.67', '39.69', '39.45', '181800']

types = [str, float, str, str, float, float, float, float, int]
converted = [func(val) for func, val in zip(types, row)]
converted[2] = tuple(converted[2].split('/')) # Bonus: convertir date en una tupla
record = dict(zip(headers, converted))
print(record) # {'name': 'AA', 'price': 39.48, 'date': ('6', '11', '2007'), 'time': '9:36am', 'change': -0.18, 'open': 39.67, 'high': 39.69, 'low': 39.45, 'volume': 181800}