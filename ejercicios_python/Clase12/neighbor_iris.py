"""
Trabajaremos con la librería sklearn de python que está diseñada para realizar tareas de aprendizaje automático. La misma trae algunos conjuntos de datos de ejemplo. Trabajaremos con el clásico ejemplo de Clasificación de Especies de flores Iris según medidas del pétalo y el sépalo.
"""
#%%
from sklearn.datasets import load_iris
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Este dataset trae una serie de datos medidos de los pétalos y sépalos de 150 flores Iris y su clasificación en tres especies (setosa, versicolor y virginica).
iris_dataset = load_iris()
print("Claves del diccionario iris_dataset:\n", iris_dataset.keys())

# %%
# El dataset es un diccionario con diferentes datos. Esencialmente en "data" tiene un array con las medidas de ancho y largo de pétalo y sépalo (atributos, o "features" en inglés) de 150 flores y en "target" tiene un numero (0, 1 ó 2) que representa la especie de estas flores. Veamos un poco la estructura de estos datos.
print("Target names:", iris_dataset['target_names'])
print("Feature names:\n", iris_dataset['feature_names'])

#%%
print("Type of data:", type(iris_dataset['data']))
print("Shape of data:", iris_dataset['data'].shape)
print("First five rows of data:\n", iris_dataset['data'][:5])
print("Type of target:", type(iris_dataset['target']))
print("Shape of target:", iris_dataset['target'].shape)
print("Target:\n", iris_dataset['target'])

#%%
# creamos un dataframe de los datos de flores
# etiquetamos las columnas usando las cadenas de iris_dataset.feature_names
iris_dataframe = pd.DataFrame(iris_dataset['data'], columns = iris_dataset.feature_names)
# y hacemos una matriz de gráficos de dispersión, asignando colores según la especie, usando pandas
# pd.plotting.scatter_matrix(iris_dataframe, c = iris_dataset['target'], figsize = (15, 15), marker = 'o', hist_kwds = {'bins': 20}, s = 60, alpha = 0.8)

# %%
# Cargamos el dataset y lo graficamos con seaborn
df = sns.load_dataset("iris")
sns.set_theme(style="ticks")
sns.pairplot(df, hue="species")

# %%
# Repetí el gráfico de pandas pero usando seaborn para graficar
iris_dataframe['target'] = iris_dataset['target']
sns.set_theme(style="ticks")
sns.pairplot(iris_dataframe, hue="target")

# %%
# training y testing
X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state = 0)

# %%
# modelar
knn = KNeighborsClassifier(n_neighbors = 1)
knn.fit(X_train, y_train)

#%%
# nueva flor
X_new = np.array([[5, 2.9, 1, 0.2]])
# print("X_new.shape:", X_new.shape)

# %%
# graficamos la nueva flor en rojo
plt.scatter(X_train[:, 1], X_train[:, 3], c = y_train)
plt.scatter(X_new[:, 1], X_new[:, 3], c = 'red')

# %%
# utilizamos el algoritmo knn entrenado para clasificar la nueva flor
prediction = knn.predict(X_new)
print("Predicción:", prediction)
print("Nombre de la Especie Predicha:",
       iris_dataset['target_names'][prediction])
       
# %%
# evaluacion del modelo
y_pred = knn.predict(X_test)
print("Predicciones para el conjunto de Test:\n", y_pred)
print("Etiquetas originales de este conjunto:\n", y_test)

# %%
# utilizamos la función score del clasificador
print("Test set score: {:.2f}".format(knn.score(X_test, y_test)))
