# Solicitar un número del 1 al 7 al usuario
numero = int(input("Ingrese un número del 1 al 7: "))

# Determinar el día de la semana
if numero == 1:
    dia = "Lunes"
elif numero == 2:
    dia = "Martes"
elif numero == 3:
    dia = "Miércoles"
elif numero == 4:
    dia = "Jueves"
elif numero == 5:
    dia = "Viernes"
elif numero == 6:
    dia = "Sábado"
elif numero == 7:
    dia = "Domingo"
else:
    dia = None

# Imprimir el resultado
if dia is not None:
    print("El día de la semana correspondiente es:", dia)
else:
    print("Número no válido. Por favor, ingrese un número del 1 al 7.")
