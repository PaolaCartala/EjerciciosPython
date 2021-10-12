"""
Al comienzo de la materia estuvimos trabajando con el dataset de árboles en parques. Ahora estuvimos analizando otro dataset: el de árboles en veredas. Ahora queremos estudiar si hay diferencias entre los ejemplares de una misma especie según si crecen en un sitio o en otro. Queremos hacer un boxplot del diámetro a la altura del pecho para las Tipas (su nombre científico es tipuana tipu), que crecen en ambos tipos de ambiente. Para eso tendremos que juntar datos de dos bases de datos diferentes.
"""

#%%
import pandas as pd
import os
import seaborn as sns

directorio = '../Data'
archivo_parques = 'arbolado-en-espacios-verdes.csv'
archivo_veredas = 'arbolado-publico-lineal-2017-2018.csv'
f_parques = os.path.join(directorio, archivo_parques)
f_veredas = os.path.join(directorio, archivo_veredas)
# levantamos los archivos en dataframes
df_parques = pd.read_csv(f_parques)
df_veredas = pd.read_csv(f_veredas)

#%%
# seleccionamos tipas con columnas diametro y altura en parque
col_parques = ['diametro', 'altura_tot']
df_tipas_parques = df_parques[col_parques][df_parques['nombre_cie'].isin(['Tipuana Tipu'])].copy()

# %%
# seleccionamos tipas con columnas diametro y altura en veredas
col_veredas = ['diametro_altura_pecho', 'altura_arbol']
df_tipas_veredas = df_veredas[col_veredas][df_veredas['nombre_cientifico'].isin(['Tipuana tipu'])].copy()

# %%
# cambiar los nombres
df_tipas_veredas.rename(columns={'diametro_altura_pecho': 'diametro', 'altura_arbol': 'altura_tot'}, inplace=True)

# %%
# agregar la columna 'ambiente' con 'parque'
df_tipas_parques = df_tipas_parques.assign(ambiente='parque')

# %%
# agregar la columna 'ambiente' con 'vereda'
df_tipas_veredas = df_tipas_veredas.assign(ambiente='vereda')

# %%
# juntar datasets
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])
print(df_tipas)

# %%
# boxplot diametro
sns.boxplot(data=df_tipas, y='diametro', x='ambiente') # boxplot con seaborn
# df_tipas.boxplot('diametro', by = 'ambiente') # boxplot con pandas

# %%
# boxplot altura
sns.boxplot(data=df_tipas, y='altura_tot', x='ambiente')
# df_tipas.boxplot('altura_tot', by = 'ambiente')
