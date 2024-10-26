# Solicitar al usuario los dos números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Realizar las operaciones aritméticas
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2

# Comprobar si se puede realizar la división
if numero2 != 0:
    division = numero1 / numero2
    print("La división es:", division)
else:
    print("No se puede dividir por cero.")

# Mostrar los resultados
print("La suma es:", suma)
print("La resta es:", resta)
print("La multiplicación es:", multiplicacion)
