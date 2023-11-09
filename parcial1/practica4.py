# Importar numpy
import numpy as np

# Crear una matriz unidimensional
matriz = np.array([10, 20, 30])

# Crear una matriz bidimensional
matriz2 = np.array([[10, 20, 30], [5, 10, 15]])

# Crear una matriz de números aleatorios enteros entre 1 y 10, de tamaño (5, 5)
matriz3 = np.random.randint(1, 10, size=(5, 5))
print(matriz3)

# Imprimir la cantidad de dimensiones de la matriz
print("El número de dimensiones del arreglo es:", matriz3.ndim)

# Imprimir la cantidad de elementos en la matriz
print("El número de elementos del arreglo es:", matriz3.size)

# Imprimir el tipo de datos de la matriz
print("El tipo de datos de la matriz es:", matriz3.dtype)

# Imprimir la suma de los elementos en la diagonal principal (traza)
print("La traza de la matriz es:", matriz3.trace())

# Imprimir la forma (shape) de la matriz
print("La forma (shape) de la matriz es:", matriz3.shape)

# Imprimir el índice del elemento máximo en la matriz
print("El índice del elemento máximo es:", matriz3.argmax())

# Imprimir el índice del elemento mínimo en la matriz
print("El índice del elemento mínimo es:", matriz3.argmin())
