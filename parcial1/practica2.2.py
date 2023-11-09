while True:
    numero_original = int(input('SELECCIONA UN NUMERO (o ingresa 0 para salir) '))

    if numero_original == 0:
        break

    def invertir_numero(numero):
        numero_invertido = 0
        while numero > 0:
            digito = numero % 10
            numero_invertido = numero_invertido * 10 + digito
            numero = numero // 10
        return numero_invertido

    numero_invertido = invertir_numero(numero_original) #RECURSIVIDAD APLICADA

    print(f"SU NUMERO ES: {numero_original} EL NUMERO INVERTIDO ES: {numero_invertido}")