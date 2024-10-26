#Ordenar una lista de cadenas por la cantidad de vocales que contiene cada cadena usando sort(), una función 
#como key y reverse=True.


def contar_vocales(cadena):
    # Función que cuenta las vocales en una cadena
    vocales = "aeiouAEIOU"  # Considerar tanto mayúsculas como minúsculas
    return sum(1 for letra in cadena if letra in vocales)

# Lista de cadenas
lista_cadenas = ["manzana", "pera", "plátano", "naranja", "uva", "fresa"]

# Ordenar la lista por la cantidad de vocales en orden descendente
lista_cadenas.sort(key=contar_vocales, reverse=True)

# Mostrar la lista ordenada
print("Lista de cadenas ordenada por la cantidad de vocales (descendente):")
print(lista_cadenas)
