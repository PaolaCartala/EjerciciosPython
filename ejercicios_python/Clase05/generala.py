"""
Queremos estimar la probabilidad de obtener una generala servida (cinco dados iguales) en una tirada de dados.
- Escribí una función tirar() que devuelva una lista con cinco dados generados aleatoriamente. Escribí otra función llamada es_generala(tirada) que devuelve True si y sólo si los cinco dados de la lista tirada son iguales.
- Si uno juega con las reglas originales (se puede volver a tirar algunos de los cinco dados hasta dos veces, llegando hasta a tres tiradas en total) siguiendo una estrategia que intente obtener generala (siempre guardar los dados que más se repiten y tirar nuevamente los demás) es más probable obtener una generala que si sólo consideramos la generala servida. Escribí una función llamada prob_generala(N) que, a partir de un parámetro N realice una simulación con N repeticiones, para estimar la probabilidad de obtener una generala al finalizar una mano de tres tiradas. La función debe devolver un número entre 0 y 1.
"""

import random
from collections import Counter

# Generala servida
def tirar():
    """
    Retorna una lista con 5 dados con valores del 1 al 6
    """
    tirada = []
    for i in range(5):
        tirada.append(random.randint(1, 6))
    return tirada

def es_generala(tirada):
    """
    Retorna True si todos los números de la tirada son iguales
    """
    numero = tirada[0]
    generala = 0
    for n in tirada:
        if numero == n:
            generala += 1
    if generala == len(tirada):
        return True
    else:
        return False

# Generala no necesariamente servida
def prob_generala(N):
    """
    Retorna la probabilidad de hacer generala servida o en 3 tiros separando los dados que tengan el número más común de la tirada y tirando los restantes, separando a su vez los dados que coinciden con el más común. Este sistema es repetido N veces según el parámetro pasado cuando se llama a la función.
    """
    generala = 0
    for _ in range(N):
            tiro = tirar()
            comun = Counter(tiro).most_common(1)
            dados_separados = []
            for _ in range(comun[0][1]):
                dados_separados.append(comun[0][0])
            for _ in range(2):
                dados_restantes = []
                for _ in range(len(tiro) - len(dados_separados)):
                    dados_restantes.append(random.randint(1, 6))
                for numero in dados_restantes:
                    if numero == comun[0][0]:
                        dados_separados.append(numero)
                        dados_restantes.remove(numero)
                    else:
                        continue
            final = dados_separados + dados_restantes
            if es_generala(final) or es_generala(tiro):
                generala += 1
    probabilidad = generala / N
    return probabilidad

print(prob_generala(1000000))