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

