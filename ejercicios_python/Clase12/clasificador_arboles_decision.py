"""
Leé sobre los clasificadores basados en arboles de decisión y luego usá el objeto clasificador clf como se usó knn.
Tanto knn como clf son clasificadores y heredan los métodos "fit", "predict" y "score" de forma que su uso es casi idéntico.
"""
#%%
from sklearn.datasets import load_iris
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

#%%
iris_dataset = load_iris()
iris_dataframe = pd.DataFrame(iris_dataset['data'], columns = iris_dataset.feature_names)

#%%
iris_dataframe['target'] = iris_dataset['target']

#%%
X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state = 0)

#%%
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

#%%
X_new = np.array([[5, 2.9, 1, 0.2]])
# print("X_new.shape:", X_new.shape)

#%%
# graficamos la nueva flor en rojo
plt.scatter(X_train[:, 1], X_train[:, 3], c = y_train)
plt.scatter(X_new[:, 1], X_new[:, 3], c = 'red')

# %%
# utilizamos el algoritmo knn entrenado para clasificar la nueva flor
prediction = clf.predict(X_new)
print("Predicción:", prediction)
print("Nombre de la Especie Predicha:",
       iris_dataset['target_names'][prediction])

# %%
# evaluacion del modelo
y_pred = clf.predict(X_test)
print("Predicciones para el conjunto de Test:\n", y_pred)
print("Etiquetas originales de este conjunto:\n", y_test)

# %%
# utilizar la función score del clasificador
print("Test set score: {:.2f}".format(clf.score(X_test, y_test)))
