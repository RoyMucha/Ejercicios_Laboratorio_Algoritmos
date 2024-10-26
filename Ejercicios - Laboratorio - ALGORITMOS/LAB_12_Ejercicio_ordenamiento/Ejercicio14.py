#Escribir una función que tome una lista de cadenas y la ordene por la longitud de las cadenas, de mayor a menor, 
#usando Bubble Sort.

# Lista de cadenas
cadenas = ["hola", "mundo", "python", "programación", "función", "algoritmo"]

print("Lista original:")
print(cadenas)

# Implementación del algoritmo Bubble Sort para ordenar por longitud
def bubble_sort_por_longitud(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Comparar longitudes de las cadenas
            if len(lista[j]) < len(lista[j + 1]):  # Cambiar el signo para ordenar de mayor a menor
                # Intercambiar si la cadena actual es más corta que la siguiente
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Ordenar la lista usando Bubble Sort por longitud de cadenas
bubble_sort_por_longitud(cadenas)

print("Lista ordenada por longitud de cadenas (de mayor a menor):")
print(cadenas)
