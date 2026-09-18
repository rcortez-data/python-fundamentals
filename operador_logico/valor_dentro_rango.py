print("*** Valor dentro de rango ***")
print()

valor = int(input("Introduce un valor entre (0 a 5): "))

valor_correcto = valor >= 0 and valor <= 5
if valor_correcto:
    print(True)
else:
    print(False)



MAXIMO = 5
MINIMO = 0
# Solicitamos un valor entre 0 y 5
dato = int(input(f"Proporciona un dato entre {MINIMO} y {MAXIMO}: "))

# Verificamos si el dato se encuentra dentro de rango
esta_dentro_rango = dato >= MINIMO and dato <= MAXIMO
print(f"Valor estan dentro de rango? {esta_dentro_rango}")
