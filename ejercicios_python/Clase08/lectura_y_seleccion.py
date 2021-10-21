"""
Vamos a trabajar ahora con el archivo 'arbolado-publico-lineal-2017-2018.csv'. 
- Levantalo y armá un DataFrame df_lineal que tenga solamente las siguiente columnas: 'nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol'
- Imprimí las diez especies más frecuentes con sus respectivas cantidades.
- Trabajaremos con las siguientes especies seleccionadas: 'Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu'
- Realizá un boxplot de los altos de los árboles.
"""

#%%
import pandas as pd
import os
import seaborn as sns

directorio = '../Data'
archivo = 'arbolado-publico-lineal-2017-2018.csv'
fname = os.path.join(directorio, archivo) # compatibilidad para distintos os
df = pd.read_csv(fname) # levanta el archivo y arma un DataFrame

#%%
# Imprimí las diez especies más frecuentes con sus respectivas cantidades.
cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol'] # columnas seleccionadas
df_lineal = df[cols_sel] # df de las columnas seleccionadas
mas_frecuentes = df_lineal['nombre_cientifico'].value_counts() # cuantas especies hay según su nombre cientifico
print(mas_frecuentes.head(10)) # imprime los primeros 10 segun cantidad de ejemplares

# %%
# especies seleccionadas
especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']
df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]
print(df_lineal_seleccion)

# %%
# boxplot
df_lineal_seleccion.boxplot('altura_arbol', by = 'nombre_cientifico')

#%%
# boxplot con seaborn diametro
sns.boxplot(data=df_lineal_seleccion, y='diametro_altura_pecho', x='nombre_cientifico')

#%%
# boxplot con seaborn altura
sns.boxplot(data=df_lineal_seleccion, y='altura_arbol', x='nombre_cientifico')

# %%
# 8.8 ejemplo de pairplot
sns.pairplot(data = df_lineal_seleccion[cols_sel], hue = 'nombre_cientifico')
