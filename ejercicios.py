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