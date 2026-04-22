cuenta = 0
numero = 30
while True:
    numero = int(input("Dime un numero: "))
    cuenta += 1
    if numero > numero:
        print("Muy alto, intenta de nuevo")
    elif numero < numero:
        print("Muy bajo, intenta de nuevo")
    else:
        print(f"¡Correcto! Lo lograste en {cuenta} intentos")
        break