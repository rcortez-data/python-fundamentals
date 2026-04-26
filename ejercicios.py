nombre = input("Dime tu nombre: ")
calificacion = input("Calificacion español: ")
calificacion_1 = input("Calificacion matematicas: ")
calificacion_2 = input("Calificacion historia: ")
calificaciones = [calificacion, calificacion_1, calificacion_2]
promedio = (int(calificaciones[0]) + int(calificaciones[1]) + int(calificaciones[2])) / int(len(calificaciones))
resultado = [nombre, promedio]
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