#BY NOMBRE

#FACTORIAL DE UN NUMERO
def factorial(num): #CREACIÓN DE FUNCIONES CON DEF
    if num == 1: #FUNCIOÓN RECURSIVA
        return 1
    else:
        return num * factorial(num-1)
print(f'EL FACTORIAL DE 5 ES {factorial(5)}')

#SUMA DE DOS NUMEROS
def suma_enteros(n):
    if n == 0:
        return 0
    else:
        return n + suma_enteros(n - 1)

resultado = suma_enteros(5)
print(resultado)


#FIBONACCI
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(10):
    print(fibonacci(i))


#FACTORIAL CON WHILE
while True:
    numero = int(input('SELECCIONA UN NUMERO (o ingresa 0 para salir): '))
    if numero == 0:
        break  
    elif numero < 0:
        print('INGRESA UN NUMERO POSITIVO')
    else:
        factorial = 1
        temp_numero = numero 
        while numero > 0:
            factorial *= numero
            numero -= 1
        print('SU NUMERO ES', temp_numero, 'SU FACTORIAL ES', factorial)