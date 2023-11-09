import random

def adivinar_numero():
    numero_objetivo = random.randint(1, 100)
    intentos = 0

    print("Adivina el número entre 1 y 100")

    while intentos < 5:
        intento = int(input("Introduce tu adivinanza: "))

        if intento == numero_objetivo:
            print(f"¡Felicidades! Adivinaste el número correcto, que es {numero_objetivo}.")
            break
        else:
            intentos += 1
            if intento < numero_objetivo:
                print("El número es mayor.")
            else:
                print("El número es menor.")
            if intentos < 5:
                print(f"Te quedan {5 - intentos} intentos.")

    if intentos == 5:
        print(f"¡Perdiste! El número correcto era {numero_objetivo}.")

if __name__ == "__main__":
    adivinar_numero()
