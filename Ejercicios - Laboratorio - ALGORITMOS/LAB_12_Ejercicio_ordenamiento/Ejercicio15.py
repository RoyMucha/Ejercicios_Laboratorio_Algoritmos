#Implementar Insertion Sort para ordenar una lista de números en orden descendente, pero solo los números pares.

# Lista de números
numeros = [10, 3, 8, 5, 2, 7, 6, 1, 4, 9]

print("Lista original:")
print(numeros)

# Implementación del algoritmo Insertion Sort para ordenar solo números pares
def insertion_sort_pares(lista):
    # Extraer los números pares en una nueva lista
    pares = [num for num in lista if num % 2 == 0]
    
    # Ordenar los números pares en orden descendente
    for i in range(1, len(pares)):
        clave = pares[i]
        j = i - 1
        while j >= 0 and pares[j] < clave:  # Cambiar el signo para orden descendente
            j -= 1
        # Insertar el número par en la posición correcta
        pares.insert(j + 1, pares.pop(i))

    # Colocar los números pares ordenados de vuelta en su posición original
    indice_pares = 0
    for k in range(len(lista)):
        if lista[k] % 2 == 0:
            lista[k] = pares[indice_pares]
            indice_pares += 1

# Ordenar la lista usando Insertion Sort para los números pares
insertion_sort_pares(numeros)

print("Lista con números pares ordenados en orden descendente:")
print(numeros)

