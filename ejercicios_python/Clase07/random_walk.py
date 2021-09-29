"""
Una caminata al azar o random walk es una formalización matemática de la trayectoria que resulta de hacer sucesivos pasos aleatorios.
Graficá 12 trayectorias en la misma figura, con diferentes colores.
Usá la estructura de subplots para graficar tres pubplots en una figura:
Arriba, grande, 12 trayectorias aleatorias.
Abajo a la izquierda la trayectoria que más se aleja del origen.
Abajo a la derecha la trayectoria que menos se aleja del origen.
"""

import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint(-1,2,largo)
    return pasos.cumsum()

N = 100000

grid = plt.GridSpec(2, 2)
plt.yticks([randomwalk(N).min() * 1.1, randomwalk(N).max() * 1.1])

# graficar 12 trayectorias
plt.subplot(grid[0, 0:])
plots = [randomwalk(N) for _ in range(12)]
plt.title('12 caminatas al azar')
plt.xticks([])
[plt.plot(walk, linewidth=0.3) for walk in plots]

def alejados(plots):
    """
    Recibe una lista con n arrays, busca el array que se aleja mas de 0 y lo devuelve, asi como tambien el array que se aleja menos de 0 y lo devuelve
    Pre: plots debe ser una lista con arrays
    Pos: la posición [0] será el array que mas se aleja de 0 de la lista y la posición [1] será el array que menos se aleja de 0 de la lista
    Inv: plot contendrá el array que tiene el valor absoluto que mas se aleja de 0, plot2 contendrá el array que tiene el valor absoluto que menos se aleja de 0
    """
    mas_se_aleja = 0
    plot = []
    plot2 = []
    for caminata in plots:
        absoluto = abs(caminata)
        if absoluto.max() > mas_se_aleja:
            mas_se_aleja = absoluto.max()
            plot = caminata
    menos_se_aleja = mas_se_aleja
    for caminata in plots:
        absoluto = abs(caminata)
        if absoluto.max() < menos_se_aleja:
            menos_se_aleja = absoluto.max()
            plot2 = caminata
    return plot, plot2

# trayectoria que mas se aleja
plt.subplot(grid[1, 0])
plt.title('La caminata que más se aleja')
plt.xticks([])
plt.plot(alejados(plots)[0], color='green', linewidth=0.09)

# trayectoria que menos se aleja
plt.subplot(grid[1, 1])
plt.title('La caminata que menos se aleja')
plt.xticks([])
plt.plot(alejados(plots)[1], color='red', linewidth=0.09)

plt.show()