def clasificar_numero(n):
    if n > 0:
        tipo = "Positivo"
    elif n < 0:
        tipo = "Negativo"
    else:
        tipo = "Cero"

    if n != 0:
        paridad = "par" if n % 2 == 0 else "impar"
        print(f"{tipo} {paridad}")
    else:
        print(tipo)

numero = int(input("Escribe un número entero: "))
clasificar_numero(numero)