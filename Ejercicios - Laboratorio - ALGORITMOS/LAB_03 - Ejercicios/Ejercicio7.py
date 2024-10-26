# Solicitar el precio original del producto
precio_original = float(input("Ingrese el precio original del producto: "))

# Solicitar la categoría del descuento
categoria = input("Ingrese la categoría del descuento (estudiante, jubilado, empleado, otro): ").lower()

# Inicializar el descuento
descuento = 0

# Determinar el porcentaje de descuento según la categoría
if categoria == "estudiante":
    descuento = 0.10  # 10%
elif categoria == "jubilado":
    descuento = 0.15  # 15%
elif categoria == "empleado":
    descuento = 0.05  # 5%
else:
    descuento = 0.00  # 0% para otros

# Calcular el precio final
precio_final = precio_original * (1 - descuento)

# Imprimir el precio final
print("El precio final después del descuento es:", precio_final)
