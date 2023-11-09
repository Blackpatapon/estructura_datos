import numpy as np

# Generar una matriz aleatoria 6x8 con valores entre 10 y 49
matrizrandom = np.random.randint(10, 50, size=(6, 8))
print("Matriz aleatoria inicial:")
print(matrizrandom)

# Preguntar si deseas insertar una nueva fila en la matriz
pregunta = input("¿Deseas insertar una nueva fila en la matriz? (S para Sí / N para No): ")

if pregunta.lower() == "s":
    nueva_fila = np.random.randint(10, 50, size=(1, 8))
    matrizrandom = np.vstack((matrizrandom, nueva_fila))
    print("Nueva matriz con la fila insertada:")
    print(matrizrandom)
elif pregunta.lower() == "n":
    print("Matriz sin cambios.")

# Pedir el número de fila al usuario
fila_numero = int(input("Ingresa el número de fila que deseas analizar (0-{}): ".format(matrizrandom.shape[0] - 1)))

# Utilizar un atributo argwhere para imprimir valores mayores a 20 en la fila seleccionada
fila_seleccionada = matrizrandom[fila_numero]
valores_mayores_20 = np.argwhere(fila_seleccionada > 20)
print("Valores mayores a 20 en la fila seleccionada:")
for indice in valores_mayores_20:
    print("Fila {}, Columna {}: {}".format(fila_numero, indice[0], fila_seleccionada[indice[0]]))

# Utilizar e imprimir el atributo ndim
print("Número de dimensiones de la matriz:", matrizrandom.ndim)

# Utilizar el atributo shape para obtener las dimensiones de la matriz
print("Dimensiones de la matriz:", matrizrandom.shape)

# Utilizar el atributo size para obtener la cantidad total de elementos en la matriz
print("Cantidad total de elementos en la matriz:", matrizrandom.size)

# Utilizar el atributo mean para calcular y imprimir el promedio de la matriz
promedio = np.mean(matrizrandom)
print("Promedio de la matriz:", promedio)
