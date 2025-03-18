import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#Descripcion de cada una de las librerias
#numpy: es una libreria que permite trabajar con arreglos multidimensionales y matrices, junto con una gran colección de funciones matemáticas de alto nivel para operar con estos arreglos.
#pandas: es una libreria que permite manipular y analizar datos de manera sencilla y eficiente.
#matplotlib: es una libreria que permite crear visualizaciones estáticas, animadas e interactivas en Python.
#sklearn: es una libreria que permite realizar tareas de minería y análisis de datos.

X = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)
y = np.array([2,4,6,8,10,12])

modelo = LinearRegression()
modelo.fit(X,y)

nueva_x = np.array([[7]])
prediccion = modelo.predict(nueva_x)
print(f"Prediccion para X=7: {prediccion[0]}")

plt.scatter(X, y, color='red')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Datos de ejemplo')
plt.show()