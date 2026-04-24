nombre = input("Escribe tu nombre:")
puesto = input("Escribe tu puesto:")
salario = float(input("Escribe tu salario:"))
informacion = {"Nombre":nombre, "Puesto":puesto, "Salario":salario}
print("Nombre: "+informacion["Nombre"])
print("Puesto: "+informacion["Puesto"])
print(f"Salario: ${informacion['Salario']:,.2f}")
