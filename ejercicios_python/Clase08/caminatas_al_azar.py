"""
Hacer una caminata de dos horas dando un paso por minuto.
Guarda la serie o DataFrame en el disco.
"""

#%%
import numpy as np
import pandas as pd

#%%
# caminata de dos horas dando un paso por minuto
idx = pd.date_range('20200923 14:00', periods = 120, freq = 'min')
s1 = pd.Series(np.random.randint(-1,2,120), index = idx)
s2 = s1.cumsum()

s2.plot()

#%%
# usar una media movil para suavizar los datos
w = 5 # ancho en minutos de la ventana
s3 = s2.rolling(w, min_periods = 1).mean()
s3.plot()

#%%
# ambas curvas en un mismo grafico para ver el efecto del suavizado
df_series_23 = pd.DataFrame([s2, s3]).T  # armo un dataframe con ambas series
df_series_23.plot()

# %%
# creamos un índice que contenga un elemento por minuto a partir del comienzo de la clase y durante 8 horas.
horas = 8
idx = pd.date_range('20200923 14:00', periods = horas*60, freq = 'min')
nombres = ['Pedro', 'Santiago', 'Juan', 'Andrés','Bartolomé','Tiago','Isca','Tadeo','Mateo','Felipe','Simón','Tomás']

#%%
# Luego usamos el módulo random de numpy para generar pasos para cada persona a cada minuto. Los acumulamos con cumsum y los acomodamos en un DataFrame, usando el índice generado antes y poniéndoles nombres adecuados a cada columna:
df_walks = pd.DataFrame(np.random.randint(-1,2,[horas*60,12]).cumsum(axis=0), index = idx, columns = nombres)
df_walks.plot()

# %%
# Ahora suavizamos los datos, usando min_periods para no perder los datos de los extremos.
w = 45
df_walk_suav = df_walks.rolling(w, min_periods = 1).mean() # datos suavizados
nsuav = ['S_' + n for n in nombres]
df_walk_suav.columns = nsuav # cambio el nombre de las columnas para los datos suavizados
df_walk_suav.plot()

# %%
# Guardar una serie o un DataFrame en el disco
df_walk_suav.to_csv('caminata_apostolica.csv')
