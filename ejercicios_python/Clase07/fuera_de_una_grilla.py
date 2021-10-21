"""
Modificá el siguiente código para reproducir el gráfico que se muestra.
"""

import matplotlib.pyplot as plt

fig = plt.figure()
grid = plt.GridSpec(2, 3)
plt.subplot(grid[0, 0:]) # define la figura de arriba
plt.plot([0,1,2],[0,1,0]) # dibuja la curva
plt.xticks([]), plt.yticks([]) # saca las marcas

plt.subplot(grid[1, 0]) # define la primera de abajo
plt.plot([0,1],[0,1])
plt.xticks([]), plt.yticks([])

plt.subplot(grid[1, 1]) # define la segunda de abajo
plt.plot([0,1],[0.5,0.5])
plt.xticks([]), plt.yticks([])

plt.subplot(grid[1, 2]) # define la tercera de abajo
plt.plot([0,1],[1,0])
plt.xticks([]), plt.yticks([])

plt.show()