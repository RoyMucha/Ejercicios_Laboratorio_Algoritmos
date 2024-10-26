#Ejercicio1. Ordenar una lista de cadenas por su longitud usando sorted() y key=len.

# Lista de cadenas
lista_cadenas = ["manzana", "kiwi", "plátano", "naranja", "uva", "fresa", "sandía"]

# Ordenar la lista por longitud de las cadenas
lista_ordenada = sorted(lista_cadenas, key=len)

# Mostrar la lista ordenada
print("Lista ordenada por longitud de cadenas:")
for cadena in lista_ordenada:
    print(cadena)
