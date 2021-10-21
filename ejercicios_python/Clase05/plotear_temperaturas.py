"""
Escribí una función plotear_temperaturas() que lea el archivo de datos temperaturas.npy (debería tener las 999 mediciones simuladas que creaste en termometro.py) y haga un histograma de las temperaturas simuladas.
"""

import matplotlib.pyplot as plt
import numpy as np

# Empezando a plotear
# Carga el archivo guardado en el ejercicio termometro.py y muestra los datos en un histograma
temperaturas = np.load('../Data/temperaturas.npy')
plt.hist(temperaturas,bins=100)
plt.show()