#Implementa una variante de Insertion Sort que ordene una lista de palabras por la cantidad de vocales que 
#contiene cada palabra.

# Lista de palabras
palabras = ["casa", "árbol", "murciélago", "auto", "flor", "perro", "gato", "elefante"]

print("Lista original:")
print(palabras)

# Función que cuenta el número de vocales en una palabra
def contar_vocales(palabra):
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    contador = 0
    for letra in palabra:
        if letra in vocales:
            contador += 1
    return contador

# Implementación de Insertion Sort para ordenar por cantidad de vocales
def insertion_sort_por_vocales(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        
        # Contar vocales en la palabra clave
        vocales_clave = contar_vocales(clave)
        
        # Mover las palabras que tienen más vocales que la clave
        while j >= 0 and contar_vocales(lista[j]) < vocales_clave:
            lista[j + 1] = lista[j]
            j -= 1
        
        # Insertar la clave en la posición correcta
        lista[j + 1] = clave

# Ordenar la lista usando Insertion Sort por cantidad de vocales
insertion_sort_por_vocales(palabras)

print("Lista ordenada por cantidad de vocales:")
print(palabras)

