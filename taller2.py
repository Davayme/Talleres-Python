import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error

#Datos de ejemplo Tamaño de la casa en pies cuadrados y numero de habitaciones
np.random.seed(42)
tamanio = np.random.randint(50, 250, 50)
habitaciones = np.random.randint(1, 5, 50)

precio = 5000 + (tamanio * 1500) + (habitaciones * 10000) + np.random.randint(-10000, 10000, 50)

datos = pd.DataFrame({'tamanio': tamanio, 'habitaciones': habitaciones, 'precio': precio})
print(datos.head())

#Dividir los Datos en Entrenamiento y Prueba
X = datos[['tamanio', 'habitaciones']]
y = datos['precio']

#Seprar datos en entrenamiento(80%) y prueba(20%)
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = LinearRegression()
modelo.fit(x_train, y_train)
#Mostrar coeficientes
print(f"Coeficientes: {modelo.coef_}")
print(f"Intercepto: {modelo.intercept_}")
y_pred = modelo.predict(x_test)


#Evaluacion del modelo
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
print(f"Error Absoluto Medio: {mae}")
print(f"Error Cuadratico Medio: {mse}")


plt.scatter(y_test, y_pred)
plt.xlabel('Precios Reales')
plt.ylabel('Precios Predichos')
plt.title('Precios Reales vs Precios Predichos')
plt.show()

#Hacer una prediccioncon nuevos datos
# Hacer una predicción con nuevos datos
nueva_casa = pd.DataFrame([[180, 3]], columns=['tamanio', 'habitaciones'])
prediccion = modelo.predict(nueva_casa)
print(f"Predicción para una casa de 180 pies cuadrados y 3 habitaciones: {prediccion[0]}")