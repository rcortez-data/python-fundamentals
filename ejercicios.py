def tabla(n):
    if n == 0:
        print("cero")
        return
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

n = int(input("Ingresa un número: "))
tabla(n)