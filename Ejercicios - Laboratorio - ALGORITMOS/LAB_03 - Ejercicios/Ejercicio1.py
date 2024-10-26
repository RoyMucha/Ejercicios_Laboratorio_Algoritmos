# Solicitar las dos palabras al usuario
palabra1 = input("Ingrese la primera palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")

# Comparar las palabras y determinar el orden alfabético
if palabra1 < palabra2:
    print("La palabra que va primero en orden alfabético es:", palabra1)
elif palabra2 < palabra1:
    print("La palabra que va primero en orden alfabético es:", palabra2)
else:
    print("Ambas palabras son iguales.")
