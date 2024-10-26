# Solicitar al usuario que introduzca una cadena
cadena = input("Introduce una cadena: ")

# Definir las vocales
vocales = "aeiouAEIOU"

# Inicializar un contador
contador_vocales = 0

# Contar las vocales en la cadena
for letra in cadena:
    if letra in vocales:
        contador_vocales += 1

# Mostrar el resultado
print("El número de vocales en la cadena es:", contador_vocales)

