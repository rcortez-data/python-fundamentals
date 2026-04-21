# ejercicio de listas con for y upper
nombres = ["ana", "luis", "maría"]
for nombre in nombres:
    print(nombre.upper())


# Ejercicio 1

frutas = ["manzana", "naranja", "uva", "pera", "mango"]

for fruta in frutas:
    if len(fruta) > 4:
        print(fruta.upper())



# Ejercicio 2

numeros = [4, 7, 2, 19, 5, 11, 3, 8]
cuenta = 0

for numero in numeros:
    if numero > 6:
        cuenta += 1
        print(numero)
print(cuenta)


# # Ejercicio 3: FizzBuzz
# Instrucciones:
# Escribe un programa que imprima los números del 1 al 50, pero con estas reglas:

# Si el número es divisible entre 3, imprime "Fizz" en lugar del número.
# Si el número es divisible entre 5, imprime "Buzz" en lugar del número.
# Si el número es divisible entre 3 y 5 al mismo tiempo, imprime "FizzBuzz".
# Si no cumple ninguna condición, imprime el número normal.

for i in range (1,51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
