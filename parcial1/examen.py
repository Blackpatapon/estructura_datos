import numpy as np
import pandas as pd

rangoMenor = int(input("Ingresa un número mínimo: "))
rangoMayor = int(input("Ahora ingresa un número mayor al anterior: "))

filas = int(input("Ingresa el número de filas: "))
columnas = int(input("Ahora ingresa el número de columnas: "))

matriz_rango = np.random.randint(rangoMenor, rangoMayor, size=(filas, columnas))

total = np.sum(matriz_rango)

print("Suma total:", total, "\n",
      "Número de dimensiones:", matriz_rango.shape, "\n",
      "Número máximo:", np.max(matriz_rango), "\n",
      "Número mínimo:", np.min(matriz_rango), "\n",
      "Promedio de los valores:", np.mean(matriz_rango), "\n",
      "Matriz: ", matriz_rango)

excel = "parcial1/titanic.ods"
hoja = "titanic"

df = pd.read_excel(excel, hoja)
print(df, "\n",
      "Número de dimensiones del dataframe:", df.ndim, "\n",
      "Cantidad de filas y columnas del arreglo:", df.shape, "\n",
      "El número de elementos del arreglo es:", df.size, "\n",
      "El tipo de dato de los elementos es:\n", df.dtypes, "\n")

print("Hombres abordo:")
hombres = df.loc[df["Sex"] == "male"]
print(hombres.head())

print("Mujeres abordo:")
mujeres = df.loc[df["Sex"] == "female"]
print(mujeres.head())

print("Mayores de edad")
edad = df.loc[df["Age"] >= 18]
print(edad.head())
