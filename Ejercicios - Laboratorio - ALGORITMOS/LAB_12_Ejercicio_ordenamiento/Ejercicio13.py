#Utilizar Merge Sort para ordenar una lista de tuplas, donde cada tupla contiene el nombre y la edad de una 
#persona. Ordenar primero por edad y luego por nombre en orden alfabético

# Lista de tuplas (nombre, edad)
personas = [
    ("Juan", 25),
    ("Ana", 22),
    ("Pedro", 30),
    ("María", 22),
    ("Luis", 25),
    ("Sofia", 28),
]

print("Lista original:")
print(personas)

# Implementación del algoritmo Merge Sort
def merge_sort(lista):
    if len(lista) > 1:
        mid = len(lista) // 2  # Encuentra el punto medio
        izquierda = lista[:mid]  # División en la mitad izquierda
        derecha = lista[mid:]    # División en la mitad derecha

        merge_sort(izquierda)  # Ordenar la mitad izquierda
        merge_sort(derecha)    # Ordenar la mitad derecha

        i = j = k = 0

        # Mezclar las dos mitades
        while i < len(izquierda) and j < len(derecha):
            # Ordenar primero por edad, luego por nombre
            if (izquierda[i][1] < derecha[j][1]) or \
               (izquierda[i][1] == derecha[j][1] and izquierda[i][0] < derecha[j][0]):
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        # Copiar los elementos restantes de izquierda
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        # Copiar los elementos restantes de derecha
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

# Ordenar la lista usando Merge Sort
merge_sort(personas)

print("Lista ordenada por edad y nombre:")
print(personas)
