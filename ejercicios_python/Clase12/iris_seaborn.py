"""
Este dataset trae una serie de datos medidos de los pétalos y sépalos de 150 flores Iris y su clasificación en tres especies (setosa, versicolor y virginica). Graficá las especies usando seaborn.
"""
#%%
from sklearn.datasets import load_iris
import pandas as pd
import seaborn as sns

iris_dataset = load_iris()

#%%
# creamos un dataframe de los datos de flores
# etiquetamos las columnas usando las cadenas de iris_dataset.feature_names
iris_dataframe = pd.DataFrame(iris_dataset['data'], columns = iris_dataset.feature_names)

# %%
# matriz de gráficos de dispersión, asignando colores según la especie, usando seaborn
iris_dataframe['target'] = iris_dataset['target']
sns.set_theme(style="darkgrid", palette='deep')
sns.pairplot(iris_dataframe, hue="target")
