#Dada una lista de números enteros, ordenar los números pares en orden ascendente y los números impares en 
#orden descendente usando sorted() y una función lambda como key.

def ordenar_pares_impares(numeros):
    # Separar números pares e impares
    pares = [num for num in numeros if num % 2 == 0]
    impares = [num for num in numeros if num % 2 != 0]

    # Ordenar los pares en orden ascendente y los impares en orden descendente
    pares_ordenados = sorted(pares)
    impares_ordenados = sorted(impares, reverse=True)

    # Combinar los resultados
    return pares_ordenados + impares_ordenados

# Lista de números enteros
lista_numeros = [5, 2, 9, 4, 1, 6, 3, 8, 7]

# Llamar a la función y mostrar el resultado
resultado = ordenar_pares_impares(lista_numeros)
print("Lista de números ordenados (pares ascendente, impares descendente):")
print(resultado)
