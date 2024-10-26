def insertion_sort(lista):
    # Recorre la lista desde el segundo elemento

    n = len(lista)    # n sera igual a la longitud de la lista  n=5
    for i in range(1,n):       #i=1 , i=2 , i=3, i=4,
        k = lista[i]  # El elemento a insertar
        j = i - 1
        
        # Desplaza los elementos mayores hacia la derecha
        while j >= 0 and lista[j] > k:
            lista[j + 1] = lista[j]
            j -= 1
        
        # Inserta el elemento en su posición correcta
        lista[j + 1] = k

# Ejemplo de uso
lista = [12, 11, 13, 5, 6]
insertion_sort(lista)
print("Lista ordenada:", lista)  
