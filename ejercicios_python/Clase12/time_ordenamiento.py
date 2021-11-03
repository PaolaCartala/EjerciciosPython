"""
La idea de este ejercicio es, nuevamente, comparar los algoritmos de ordenamiento que vimos hasta ahora pero usando timeit() en lugar de contando a mano la cantidad de operaciones.
"""
#%%
import random
import matplotlib.pyplot as plt
import timeit as tt
import numpy as np

def generar_lista(n):
    """
    Genera una lista con n cantidad de números aleatorios
    """
    lista = [random.randint(1, 1000) for _ in range(n)]
    return lista

def generar_listas(Nmax):
    listas = [generar_lista(Nmax) for _ in range(Nmax)]
    return listas

# print(generar_listas(10))

#%%
def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    for i in range(len(lista) - 1):
        if lista[i + 1] < lista[i]:
            reubicar(lista, i + 1)
    return lista

#%%
def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista[p]

    j = p
    while j > 0 and v < lista[j - 1]:
        lista[j] = lista[j - 1]
        j -= 1

    lista[j] = v

#%%
def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    n = len(lista) - 1
    while n > 0:
        p = buscar_max(lista, 0, n)
        lista[p], lista[n] = lista[n], lista[p]
        n = n - 1
    return lista

#%%
def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""
    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max

#%%
def ord_burbujeo(lista):
    """
    Ordena los números de lista por burbujeo
    """
    for _ in range(len(lista)):
        for i in range(len(lista) - 1):
            if lista[i + 1] < lista[i]:
                v = lista[i + 1]
                j = i + 1
                lista[j] = lista[j - 1]
                j -= 1
                lista[j] = v
    return lista

#%%
def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq = merge_sort(lista[:medio])
        der = merge_sort(lista[medio:])
        lista_nueva = merge(izq, der)
    return lista_nueva

def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []
    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado

#%%
def experimento_timeit(Nmax):
    """
    Devuelve listas de tiempos de cada algoritmo de ordenamiento:
    tiempos_seleccion, tiempos_burbujeo, tiempos_insercion, tiempos_merge
    """
    global lista
    tiempos_seleccion = []
    tiempos_burbujeo = []
    tiempos_insercion = []
    tiempos_merge = []
    for lista in generar_listas(Nmax):
        tiempo_seleccion = tt.timeit('ord_seleccion(lista.copy())', number = Nmax, globals = globals())
        tiempos_seleccion.append(tiempo_seleccion)
        tiempo_burbujeo = tt.timeit('ord_burbujeo(lista.copy())', number = Nmax, globals = globals())
        tiempos_burbujeo.append(tiempo_burbujeo)
        tiempo_insercion = tt.timeit('ord_insercion(lista.copy())', number = Nmax, globals = globals())
        tiempos_insercion.append(tiempo_insercion)
        tiempo_merge = tt.timeit('merge_sort(lista.copy())', number = Nmax, globals = globals())
        tiempos_merge.append(tiempo_merge)
    
    tiempos_seleccion = np.array(tiempos_seleccion)
    tiempos_burbujeo = np.array(tiempos_burbujeo)
    tiempos_insercion = np.array(tiempos_insercion)
    tiempos_merge = np.array(tiempos_merge)

    return tiempos_seleccion, tiempos_burbujeo, tiempos_insercion, tiempos_merge

#%%
# graficamos los timepos de cada algoritmo
Nmax = 100
tiempos_seleccion, tiempos_burbujeo, tiempos_insercion, tiempos_merge = experimento_timeit(Nmax)

plt.plot(tiempos_seleccion,label = 'Comparaciones selección')
plt.plot(tiempos_insercion,label = 'Comparaciones inserción')
plt.plot(tiempos_burbujeo,label = 'Comparaciones burbujeo')
plt.plot(tiempos_merge,label = 'Comparaciones merge')
plt.xlabel("Largo de la lista")
plt.ylabel("Tiempo")
plt.title("Complejidad de la Búsqueda")
plt.legend()
plt.show()
