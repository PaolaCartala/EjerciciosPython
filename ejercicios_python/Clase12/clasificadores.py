"""
Repetí 100 veces lo siguiente y calculá el promedio de los scores:
- Partición del conjunto original en test y train aleatoriamente (sin fijar la semilla).
- Entrenamiento de ambos modelos (knn y clf) con el conjunto train resultante.
- Evaluación de ambos clasifcadores (score) con el conjunto test resultante.
Imprimí el promedio de los scores obtenidos.
"""
#%%
from sklearn.datasets import load_iris
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

#%%
def iris_loader():
    """
    Carga el dataset iris.
    """
    iris_dataset = load_iris()
    iris_dataframe = pd.DataFrame(iris_dataset['data'], columns = iris_dataset.feature_names)
    iris_dataframe['target'] = iris_dataset['target']
    return iris_dataset

#%%
def partition():
    """
    Realiza la partición del dataset y devuelve X_train, X_test, y_train, y_test aleatoriamente.
    """
    iris_dataset = iris_loader()
    X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'])
    return X_train, X_test, y_train, y_test

#%%
def training_knn(X_train, y_train):
    """
    Entrena los conjuntos con el algoritmo "vecinos más cercanos".
    """
    knn = KNeighborsClassifier(n_neighbors = 1)
    knn.fit(X_train, y_train)
    return knn

#%%
def training_clf(X_train, y_train):
    """
    Entrena los conjuntos con el algoritmo "clasificador de árbol de decisión".
    """
    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)
    return clf

#%%
def testing(knn, clf):
    """
    Evalúa los clasificadores knn y clf y devuelve los scores y_test_knn e y_test_clf.
    """
    y_test_knn = clf.score(X_test, y_test)
    y_test_clf = knn.score(X_test, y_test)
    return y_test_knn, y_test_clf

#%%
# realizamos pruebas aleatorias e imprimimos el promedio
pruebas = 100
scores = 0
for _ in range(pruebas):
    X_train, X_test, y_train, y_test = partition()
    knn = training_knn(X_train, y_train)
    clf = training_clf(X_train, y_train)
    scores += testing(knn, clf)[0]
    scores += testing(knn, clf)[1]
    promedio = scores / (pruebas * 2)
print(f'El promedio de scores es: {promedio.round(5)}')
