numeros = input("Ingresa una serie de números separados por comas: ")
lista_numeros = numeros.split(",")
suma = 0
cantidad = 0

for numero in lista_numeros:
    suma += float(numero)  # Convertir a float y sumar
    cantidad += 1  # Contar la cantidad de números

if cantidad > 0:
    promedio = suma / cantidad
    print("El promedio es:", promedio)
else:
    print("No se ingresaron números.")
