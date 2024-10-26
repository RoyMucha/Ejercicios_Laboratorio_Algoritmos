#Ordenar una lista de números aleatorios usando Bubble Sort.

import random

# Generar una lista de números aleatorios
numeros = [random.randint(1, 100) for _ in range(10)]

print("Lista original:")
print(numeros)

# Implementación del algoritmo Bubble Sort
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                # Intercambiar si el elemento encontrado es mayor que el siguiente
                lista[j], lista[j+1] = lista[j+1], lista[j]

# Ordenar la lista usando Bubble Sort
bubble_sort(numeros)

print("Lista ordenada:")
print(numeros)
