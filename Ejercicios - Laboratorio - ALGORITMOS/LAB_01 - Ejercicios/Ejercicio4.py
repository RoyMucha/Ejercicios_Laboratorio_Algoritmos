# Definir el radio del círculo
radio = 30

# Definir el valor de pi
pi = 3.14

# Calcular el área del círculo
area_of_circle = pi * (radio ** 2)

# Calcular la circunferencia del círculo
circum_of_circle = 2 * pi * radio

# Imprimir los resultados para el radio de 30 metros
print("Para un círculo con un radio de 30 metros:")
print("Área del círculo:", area_of_circle)
print("Circunferencia del círculo:", circum_of_circle)

# Solicitar al usuario que ingrese el radio
radio_usuario = float(input("Ingrese el radio del círculo en metros: "))

# Calcular el área usando el radio ingresado por el usuario
area_usuario = pi * (radio_usuario ** 2)

# Imprimir el área calculada con el radio ingresado por el usuario
print("El área del círculo con radio", radio_usuario, "metros es:", area_usuario)
