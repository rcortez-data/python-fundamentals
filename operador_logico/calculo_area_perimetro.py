# Calculo de Area y Perimetro de un rectangulo

altura = float(input("Ingrese la altura del rectangulo: "))
base = float(input("Ingrese la base del rectangulo: "))

calculo_area = base * altura
print(f"\nEl area del rectangulo es: {calculo_area}")

calculo_perimetro = 2 * (base + altura)
print(f"\nEl perimetro del rectangulo es: {calculo_perimetro}")
