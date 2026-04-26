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

# # Ejercicio 4
# Instrucciones:
# Escribe un programa donde:
# Tienes un número secreto fijo (puedes usar el que quieras, ej. 42).
# El programa le pide al usuario que adivine con input().
# Si el número es muy bajo, imprime "Muy bajo, intenta de nuevo".
# Si el número es muy alto, imprime "Muy alto, intenta de nuevo".
# Si adivina, imprime "¡Correcto! Lo lograste en X intentos" y el programa termina.
# El programa sigue preguntando hasta que adivine.

cuenta = 0
num = 30
while True:
    numero = int(input("Dime un numero: "))
    cuenta += 1
    if numero > num:
        print("Muy alto, intenta de nuevo")
    elif numero < num:
        print("Muy bajo, intenta de nuevo")
    else:
        print(f"¡Correcto! Lo lograste en {cuenta} intentos")
        break


# ejercicio #5

nombre = input("Escribe tu nombre:")
puesto = input("Escribe tu puesto:")
salario = float(input("Escribe tu salario:"))
informacion = {"Nombre":nombre, "Puesto":puesto, "Salario":salario}
print("Nombre: "+informacion["Nombre"])
print("Puesto: "+informacion["Puesto"])
print(f"Salario: ${informacion['Salario']:,.2f}")


# Ejercicio #6

nombre = input("Dime tu nombre: ")
calificacion = input("Calificacion español: ")
calificacion_1 = input("Calificacion matematicas: ")
calificacion_2 = input("Calificacion historia: ")
calificaciones = [calificacion, calificacion_1, calificacion_2]
promedio = (int(calificaciones[0]) + int(calificaciones[1]) + int(calificaciones[2])) / len(calificaciones)
if promedio >=  90:
    estado = ("Excelente")
elif promedio > 69:
    estado = ("Aprobado")
elif promedio > 59:
    estado = ("En riesgo")
else:
    estado = ("Reprobado")
reporte = {"nombre": nombre, "promedio": promedio, "estado": estado}
print(f"""
=============================
Nombre  : {reporte["nombre"]}
Promedio: {reporte["promedio"]}
Estado  : {reporte["estado"]}
=============================
""")

# Ejercicio #7

# Clasificador de números
# Escribe un programa que:

# Le pida al usuario que ingrese un número
# Determine e imprima si el número es:

# Positivo, negativo o cero
# Par o impar (solo si no es cero)
# Grande (mayor a 1000), mediano (entre 100 y 1000) o pequeño (menor a 100) — en valor absoluto

num = int(input("Dime un numero: "))

# Positivo / negativo / cero
if num > 0:
    tipo = "positivo"
elif num < 0:
    tipo = "negativo"
else:
    tipo = "cero"

# Par o impar
if num != 0:
    if num % 2 == 0:
        paridad = "par"
    else:
        paridad = "impar"
else:
    paridad = None

# Tamaño
if abs(num) >= 1000:
    tamaño = "grande"
elif abs(num) >= 100:
    tamaño = "mediano"
else:
    tamaño = "pequeño"

print(f"El número es {tipo}.")
if paridad is not None:
    print(f"El número es {paridad}.")
print(f"El número es {tamaño}.")