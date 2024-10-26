# Pedir al usuario que ingrese un número entero positivo
numero = int(input("Ingresa un número entero positivo: "))

# Imprimir la tabla de multiplicar del número
print("Tabla de multiplicar de", numero)

# Usar un bucle for para generar la tabla de multiplicar
for i in range(1, 11):  # Multiplicamos del 1 al 10
    resultado = numero * i
    print(numero, "x", i, "=", resultado)

