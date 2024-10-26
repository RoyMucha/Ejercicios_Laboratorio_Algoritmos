# Solicitar el nombre del usuario
nombre = input("Ingrese su nombre: ")

# Solicitar el apellido del usuario
apellido = input("Ingrese su apellido: ")

# Encontrar la longitud del nombre y apellido
longitud_nombre = len(nombre)
longitud_apellido = len(apellido)

# Comparar las longitudes y mostrar el resultado
if longitud_nombre > longitud_apellido:
    print("El nombre es más largo que el apellido.")
elif longitud_nombre < longitud_apellido:
    print("El apellido es más largo que el nombre.")
else:
    print("El nombre y el apellido tienen la misma longitud.")