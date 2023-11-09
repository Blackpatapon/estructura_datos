def suma_digitos(numero):
    suma = 0
    while numero > 0:
        digito = numero % 10
        suma += digito
        numero = numero // 10
    return suma

while True:
    numero = int(input("SELECCIONA UN NUMERO (o ingresa 0 para salir) "))

    if numero == 0:
        break

    resultado = suma_digitos(numero) #RECURSIVIDAD APLICADA
    print(f"LA SUMA DE LOS DIGITOS DEL NUMERO {numero} ES {resultado}")