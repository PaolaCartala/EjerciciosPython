# -*- coding: utf-8 -*-
"""
Consideramos datos de precios (en miles de pesos) de alquiler mensual de departamentos en el barrio de Caballito, CABA, y sus superficies (en metros cuadrados). Queremos modelar el precio de alquiler a partir de la superficie para este barrio.
- Ajustá los datos con una recta.
- Graficá los datos junto con la recta del ajuste.
Una forma de cuantificar cuán bien ajusta la recta es considerar el promedio de los errores cuadráticos, llamado error cuadrático medio. Calculá el error cuadrático medio del ajuste.
"""
#%%
import numpy as np
import matplotlib.pyplot as plt

#%
def ajuste_lineal_simple(x,y):
    """
    Ajusta los datos
    """
    a = sum(((x - x.mean())*(y-y.mean()))) / sum(((x-x.mean())**2))
    b = y.mean() - a*x.mean()
    return a, b
#%
superficie = np.array([150.0, 120.0, 170.0, 80.0])
alquiler = np.array([35.0, 29.6, 37.4, 21.0])

#%%
# gráfico simple de los datos
g = plt.scatter(x = superficie, y = alquiler)
plt.xlabel('superficie')
plt.ylabel('alquiler')
plt.show()

#%%
# gráfico con la recta del ajuste
a, b = ajuste_lineal_simple(superficie, alquiler)
minx = 0
maxx = 200
grilla_x = np.linspace(start = minx, stop = maxx)
grilla_y = grilla_x*a + b

g = plt.scatter(x = superficie, y = alquiler)
plt.title('alquiler ajuste lineal')
plt.plot(grilla_x, grilla_y, c = 'green')
plt.xlabel('superficie')
plt.ylabel('alquiler')

plt.show()

#%%
# error cuadrático medio
errores = alquiler - (a*superficie + b)
print(errores)
print("ECM:", (errores**2).mean())
# %%
