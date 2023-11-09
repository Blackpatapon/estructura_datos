#CREACION DE ARREGLO BIDIMENCISIONAL
arreglo = [['juan','fernando'],[1,2,3]] #imprime elemento fernando

#RECORRER TODo EL ARREGLO
#ACCEDEMOS A LAS FILAS
for fila in arreglo:
    #ACCEDEMOS A CADA COLUMNA DENTRI DE FILA
    for columna in fila:
        print(columna)

print(arreglo[0][1])
print(arreglo[1][1])

n_veces = int(input('Ingrese el número de personas: '))

arreglo2 = [[],[],[]]

for i in range(n_veces):
    print('INGRESA LA INFORMACIÓN DE LA PERSONA', i + 1)
    nombre = input('INGRESA NOMBRE: ')
    edad = int(input('INGRESA EDAD: '))
    pais = input('DE QUE PAIS RESIDE: ')

    arreglo2[0].append(nombre)
    arreglo2[1].append(edad)
    arreglo2[2].append(pais)

for i in range(n_veces):
    print('DATOS DE LA PERSONA', i + 1)
    print('EL NOMBRE ES:', arreglo2[0][i])
    print('LA EDAD ES:', arreglo2[1][i])
    print('EL PAIS DE ORIGEN ES: ',arreglo2[2][i])



