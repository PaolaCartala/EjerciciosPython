"""
Definí una función generar_lista(N) que genere una lista aleatoria de largo N con números enteros del 1 al 1000 (puede haber repeticiones).
Copiá en tu programa el código de las tres funciones de ordenamiento y modificalas para que cuenten cuántas comparaciones entre elementos de la lista realiza cada una.
- Realizá un experimento que genere una lista de largo N y la ordene con los tres métodos (burbujeo, inserción y selección). Definí una función experimento(N, k) que repita k veces lo siguiente: generar una lista de largo N, ordenar la lista con los tres métodos y guardar la cantidad de operaciones.
- Definí una función experimento_vectores(Nmax) que para N entre 1 y Nmax genere una lista de largo N con números enteros del 1 al 1000 en orden aleatorio, calcule la cantidad de comparaciones realizadas por cada método de ordenamiento y guarde estos resultados en tres vectores. Graficá estos tres vectores. Si las curvas se superponen, graficá una de ellas con línea punteada para poder verlas bien.
"""
#%%
import random
import matplotlib.pyplot as plt

def generar_lista(n):
    """
    Genera una lista con n cantidad de números aleatorios
    """
    lista = [random.randint(1, 1000) for _ in range(n)]
    return lista

#%%
def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    contador = 0
    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
            reubicar(lista, i + 1)
            contador += 1
        # print("DEBUG: ", lista)

    return contador

#%%
def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista[p]

    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1

    lista[j] = v

#%%
def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    # contador
    contador = 0
    # posición final del segmento a tratar
    n = len(lista) - 1
    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p = buscar_max(lista, 0, n)
        contador += 1

        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]
        # print("DEBUG: ", p, n, lista)

        # reducir el segmento en 1
        n = n - 1

    return contador

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
    contador = 0
    for _ in range(len(lista)):
        for i in range(len(lista) - 1):
            if lista[i + 1] < lista[i]:
                v = lista[i + 1]
                j = i + 1
                lista[j] = lista[j - 1]
                j -= 1
                lista[j] = v
                contador += 1
                # print("DEBUG: ", lista)
    return contador

#%%
def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    contador = 0
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq = merge_sort(lista[:medio])[0]
        der = merge_sort(lista[medio:])[0]
        lista_nueva = merge(izq, der)[0]
        contador = merge(izq, der)[1]
    return lista_nueva, contador

def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []
    contador = 0
    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
            contador += 1
        else:
            resultado.append(lista2[j])
            j += 1
            contador += 1


    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado, contador

#%%
def experimento(n, k):
    """
    Genera k veces una lista de largo n y las ordena según los métodos de seleccion, burbujeo e inserción, luego devuelve el promedio de la cantidad de comparaciones que realizaron todos los métodos.
    """
    contador = 0
    for _ in range(k):
        lista = generar_lista(n)
        contador += ord_burbujeo(lista.copy())
        contador += ord_insercion(lista.copy())
        contador += ord_seleccion(lista.copy())
        contador += merge_sort(lista.copy())[1]
    return contador / (3 * k)

print(experimento(10, 100))

#%%
def experimento_vectores(Nmax):
    """
    Grafica la cantidad de comparaciones que hace cada método para ordenar una lista Nmax de números aleatorios.
    """
    comparaciones_seleccion = []
    comparaciones_insercion = []
    comparaciones_burbujeo = []
    comparaciones_merge = []
    for n in range(Nmax):
        lista = generar_lista(n)
        comparaciones_seleccion.append(ord_seleccion(lista.copy()))
        comparaciones_insercion.append(ord_insercion(lista.copy()))
        comparaciones_burbujeo.append(ord_burbujeo(lista.copy()))
        comparaciones_merge.append(merge_sort(lista.copy())[1])
    plt.plot(range(Nmax),comparaciones_seleccion,label = 'Comparaciones selección')
    plt.plot(range(Nmax),comparaciones_insercion,label = 'Comparaciones inserción', linestyle='dashdot')
    plt.plot(range(Nmax),comparaciones_burbujeo,label = 'Comparaciones burbujeo')
    plt.plot(range(Nmax),comparaciones_merge,label = 'Comparaciones merge', linestyle='dotted')
    plt.xlabel("Largo de la lista")
    plt.ylabel("Cantidad de comparaciones")
    plt.title("Complejidad de la Búsqueda")
    plt.legend()
    plt.show()

experimento_vectores(20)
