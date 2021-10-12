"""
En este práctico vamos a visualizar y analizar datos de mareas en el Río de la Plata.
- Para esto, utilizaremos el archivo 'OBS_SHN_SF-BA.csv' de la carpeta /Data.
- Podemos desplazar (shift en inglés) una Serie de Pandas usando el método ds.shift(pasos).
- Buscá los valores de delta_t (es un número entero, son pasos) y delta_h (puede tener decimales, es un float) que hacen que los dos gráficos se vean lo más similares posible.
"""
#%%

import pandas as pd

df = pd.read_csv('../Data/OBS_SHN_SF-BA.csv')

# %%
# tomar la columna Time como indice y que se interprete como timestamp
df = pd.read_csv('../Data/OBS_SHN_SF-BA.csv', index_col=['Time'], parse_dates=True)

# %%
# hacemos una copia de un fragmento
dh = df['12-25-2014':].copy()

# %%
# desplazamos la serie con shift y movemos el gráfico con ds y cte
delta_t = -1 # tiempo que tarda la marea entre ambos puertos
delta_h = 24.7 # diferencia de los ceros de escala entre ambos puertos
pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T.plot()
