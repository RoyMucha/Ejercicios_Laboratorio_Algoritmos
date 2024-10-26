# Pedir al usuario que ingrese una cadena
cadena = input("Ingresa una cadena: ")

# Pedir al usuario los índices de inicio y fin
inicio = int(input("Ingresa el índice de inicio: "))
fin = int(input("Ingresa el índice de fin: "))

# Extraer la subcadena
subcadena = cadena[inicio:fin]

# Imprimir la subcadena resultante
print("Subcadena extraída:", subcadena)
