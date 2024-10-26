#Dado un array de números enteros, ordénalo usando Bubble Sort y muestra cada paso del proceso de ordenamiento.

# Array de números enteros
numeros = [64, 34, 25, 12, 22, 11, 90]

print("Array original:")
print(numeros)

# Implementación del algoritmo Bubble Sort
def bubble_sort_mostrando_pasos(lista):
    n = len(lista)
    for i in range(n):
        # Bandera para detectar si se realizaron intercambios
        intercambiado = False
        for j in range(0, n - i - 1):
            # Comparar elementos adyacentes
            if lista[j] > lista[j + 1]:
                # Intercambiar si el elemento actual es mayor que el siguiente
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambiado = True
        # Mostrar el estado del array después de cada pasada
        print(f"Paso {i + 1}: {lista}")
        # Si no se realizaron intercambios, el array ya está ordenado
        if not intercambiado:
            break

# Ordenar el array usando Bubble Sort y mostrar cada paso
bubble_sort_mostrando_pasos(numeros)

print("Array ordenado:")
print(numeros)
