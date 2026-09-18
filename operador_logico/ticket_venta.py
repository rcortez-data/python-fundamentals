print("*** Generacion Ticket Venta ***")

precio_leche = float(input("Precio leche: "))
precio_pan = float(input("Precio pan: "))
precio_lechuga = float(input("Precio lechuga: "))
precio_platanos = float(input("Precio platanos: "))
descuento_porcentaje = int(input("Aplicar algun descuento (%)? "))

# Calculo del subtotal (Sin impuestos)
subtotal = precio_leche + precio_pan + precio_lechuga + precio_platanos

# Aplicar el descuento
descuento = subtotal * (descuento_porcentaje / 100)

# Subtotal con descuento
subtotal_con_descuento = subtotal - descuento

# Calculo con impuestos (16%)
impuesto = subtotal_con_descuento * 0.16

#  Calculo total de la compra (con impuestos)
costo_total_compra = subtotal_con_descuento + impuesto
print(f"""
subtotal: ${subtotal:.2f}
descuento: ${descuento:.2f} ({descuento_porcentaje}%)
subtotal con descuento: ${subtotal_con_descuento:.2f}
impuesto (16%): ${impuesto:.2f}
Costo total de la compra: ${costo_total_compra:.2f}
""")

