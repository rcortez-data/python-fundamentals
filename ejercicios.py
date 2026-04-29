for i in range(1, int(input("Dime un numero: "))+1):

    num = i

    if num % 2 == 0:
        paridad = "par"
    else:
        paridad = "impar"
    print(f"{i} {paridad}")
