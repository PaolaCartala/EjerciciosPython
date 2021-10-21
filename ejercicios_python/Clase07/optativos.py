"""
Gráficos de barras: Modificá el siguiente código para generar un gráfico similar al que se muestra: tenés que agregar etiquetas para las barras rojas cuidando la alineación del texto.

Coordenadas polares: A partir de este código, generá un gráfico como el siguiente.

Setear el color de un scatter plot: Modificá el código que sigue para generar un gráfico similar al que se muestra, prestando atención a los límites, el tamaño de las marcas, el color, y la transparencia de los trazos.
"""

import matplotlib.pyplot as plt
import numpy as np

"""
# Gráficos de barras
n = 12
X = np.arange(n) # crea vectores con elementos equiespaciados de 0 a n
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

for x, y in zip(X, Y1):
    plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='right', va= 'bottom')
for x, y in zip(X, Y2): # muestra las etiquetas rojas
    plt.text(x + 0.4, -y - 0.05, '%.2f' % y, ha='right', va= 'top')

plt.ylim(-1.25, 1.25)
plt.xticks([]), plt.yticks([]) # saca las marcas de los ejes
"""

"""
# Coordenadas polares
axes = plt.axes([0.02, 0.02, 0.97, 0.97], polar=True) # polar=True If True, equivalent to projection='polar'

N = 20
theta = np.arange(0., 2 * np.pi, 2 * np.pi / N)
radii = 10 * np.random.rand(N)
width = np.pi / 4 * np.random.rand(N)
bars = plt.bar(theta, radii, width=width, bottom=0.0)

for r, bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.jet(r / 10.))
    bar.set_alpha(0.5)

axes.set_yticklabels([]), axes.set_xticklabels([]) # saca las marcas de los ejes

"""

# Setear el color de un scatter plot
n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
color = np.arctan2(Y, X) # Arco tangente de elementos de Y/X
plt.scatter(X,Y, s=150, c=color, alpha=0.3) # s=shape, c=color, alpha=transparencia
plt.xticks([]), plt.yticks([]) # saca las marcas de los ejes
plt.ylim(-1.25, 1.25) # rango eje y
plt.xlim(-1.25, 1.25) # rango eje x

plt.show()