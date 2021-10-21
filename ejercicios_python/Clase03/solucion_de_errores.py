# solucion_de_errores.py
"""
En los siguientes ejercicios te proponemos que uses las técnicas para resolver los problemas que aparecen a continuación. Determiná los errores de los siguientes códigos y corregilos comentando brevemente los errores. ¿Qué tipo de errores tiene cada uno?

Separá las correcciones de los distintos códigos con una línea que contenga solamente los símbolos #%% seguido de una o varias líneas comentadas indicando el ejercicio y el problema que tenía
"""

# %%
# Ejercicio 3.1 Semántica
# Comentario: el error era de tipo semántico.
# Saqué el else del if, ya que la condición se evaluaba en el else retornando False y la iteración terminaba, por lo que sólo se evaluaba la posición 0 del string, pasé el return False como parte de la función cuando while evaluaba como falsa su condición, por lo tanto cuando se termina de iterar la expresión y nunca evalúa como True en el if, sale del while y evalúa como False.
# No funcionaba en todos los casos porque solo evaluaba 'a' como minúscula, por lo que agregué la opción de evaluarla como 'A'.

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a' or expresion[i] == 'A':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')

# %%
# Ejercicio 3.2 Sintaxis
# Comentario: el error era de tipo sintáctico.
# Faltaban los : tanto en la definición de la función, como en el while y el if. Además al evaluar la condición en el if no se comparaba si la expresión era igual a 'a', sino que se igualaba la expresión a 'a' con un solo signo =, y por último en el return del while, False estaba escrito como Falso.

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')

# %%
# Ejercicio 3.3 Tipos
# Comentario: error de tiempo de ejecución.
# Cuando se evalúa el caso en el que el parámetro es 1984, la variable n da error ya que el objeto int no tiene len(), para solucionarlo normalicé el argumento a string en expresion_string con la función str() y lo reemplacé por expresion en toda la función.

def tiene_uno(expresion):
    expresion_string = str(expresion)
    n = len(expresion_string)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion_string[i] == '1':
            tiene = True
        i += 1
    return tiene

tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)

# %%
# Ejercicio 3.4 Alcances
# Comentario: error de scope
# No era posible acceder a la variable c que estaba dentro de la función, por lo que la cambié por un return para que se devuelva la suma de los argumentos.

def suma(a,b):
    return a + b

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")
