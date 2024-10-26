def merge_sort(lista):
    if len(lista) > 1:
        # Dividimos la lista en dos mitades
        mid = len(lista) // 2
        izquierda = lista[:mid]
        derecha = lista[mid:]

        # Llamada recursiva para ordenar ambas mitades
        merge_sort(izquierda)
        merge_sort(derecha)

        # Índices para las dos mitades
        i = j = k = 0

        # Combinar las dos mitades
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        # Verificamos si quedó algún elemento en la mitad izquierda
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        # Verificamos si quedó algún elemento en la mitad derecha
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

# Ejemplo de uso
lista = [38, 27, 43, 3, 9, 82, 10]
merge_sort(lista)
print("Lista ordenada:", lista)  # Salida: [3, 9, 10, 27, 38, 43, 82]
