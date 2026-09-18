print("*** Operador not ***")

condicion1 = False
resultado = not condicion1
print(f"Operador not sobre {condicion1} es {resultado}")

# Revisar si una variable es cadena vacia
nombre = "juan"
es_cadena_vacia = not nombre
print(f"\nLa variable no tiene ningun valor? {es_cadena_vacia}")

# Revisar si una variable no tiene ningun valor asignado
variable = None
es_variable_sin_valor = not variable
print(f"\nLa variable no tiene ningun valor asignado? {es_variable_sin_valor}")

# Dentro rango not
# Revisar si una variable se encuentra dentro de rango 1 y 10
dato = int(input("Proporciona un dato entero: "))

# Revisamos si esta dentro de rango
esta_dentro_rango = 1 <= dato <= 10
print(f"\nVariable esta dentro de rango (entre 1 y 10)? {esta_dentro_rango}")

# Revisamos la logica inversa, para saber si el dato esta fuera de rango

esta_fuera_rango = not(1 <= dato <= 10)
print(f"\nVariable esta fuera de rango (entre 1 y 10)? {esta_fuera_rango}")