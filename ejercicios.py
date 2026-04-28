numero = int(input("Escribe un numero entero positivo: "))

suma = 0 

for num in range(1, numero + 1):
    suma += num 
    print(num)
print("La suma es: ", suma)