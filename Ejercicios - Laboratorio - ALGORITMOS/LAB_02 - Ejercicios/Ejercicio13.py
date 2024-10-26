# Solicitar al usuario que introduzca una cadena
cadena = input("Introduce una cadena: ")

# Contar el número de palabras
# Se utiliza el método split() que divide la cadena en palabras
palabras = cadena.split()

# Calcular el número de palabras
numero_de_palabras = len(palabras)

# Mostrar el resultado
print("El número de palabras en la cadena es:", numero_de_palabras)
