# Solicitar al usuario tres números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

# Determinar cuál es el mayor
if numero1 >= numero2:
    if numero1 >= numero3:
        mayor = numero1
    else:
        mayor = numero3
else:
    if numero2 >= numero3:
        mayor = numero2
    else:
        mayor = numero3

# Imprimir el resultado
print("El número mayor es:", mayor)
