def numero(n):
    for i in range(1,11):
        print(f'{n} x {i} = {n*i}')
n = int(input("Ingresa un número: "))
numero(n)