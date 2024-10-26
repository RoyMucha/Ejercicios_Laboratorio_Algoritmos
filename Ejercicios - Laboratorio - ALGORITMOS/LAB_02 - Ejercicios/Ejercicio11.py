# Solicitar al usuario que introduzca una cadena
cadena = input("Introduce una cadena: ")

# Eliminar espacios y convertir a minúsculas para la comparación
cadena_limpia = cadena.replace(" ", "").lower()

# Verificar si la cadena es un palíndromo
if cadena_limpia == cadena_limpia[::-1]:
    print("La cadena es un palíndromo.")
else:
    print("La cadena NO es un palíndromo.")
