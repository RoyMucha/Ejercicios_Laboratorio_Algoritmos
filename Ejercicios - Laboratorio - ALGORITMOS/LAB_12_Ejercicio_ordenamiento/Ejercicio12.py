#Implementar Insertion Sort para ordenar una lista de nombres en orden alfabético inverso.

# Lista de nombres
nombres = ["Juan", "María", "Pedro", "Ana", "Luis", "Sofia"]

print("Lista original:")
print(nombres)

# Implementación del algoritmo Insertion Sort
def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        clave = lista[i]
        j = i - 1
        # Mover los elementos de lista[0..i-1] que son mayores que clave a una posición adelante
        while j >= 0 and lista[j] < clave:  # Cambiar el signo para orden inverso
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave

# Ordenar la lista usando Insertion Sort en orden alfabético inverso
insertion_sort(nombres)

print("Lista ordenada en orden alfabético inverso:")
print(nombres)
