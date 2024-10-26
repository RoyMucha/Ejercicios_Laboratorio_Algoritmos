#Escribir una función que tome una lista de palabras y la ordene alfabéticamente por la última letra de cada palabra 
#usando sorted() y una función lambda como key.

def ordenar_por_ultima_letra(palabras):
    # Ordenar la lista de palabras por la última letra usando sorted() y una función lambda
    palabras_ordenadas = sorted(palabras, key=lambda palabra: palabra[-1])
    
    return palabras_ordenadas

# Lista de palabras
lista_palabras = ["manzana", "pera", "plátano", "naranja", "uva", "fresa"]

# Llamar a la función y mostrar el resultado
resultado = ordenar_por_ultima_letra(lista_palabras)
print("Lista de palabras ordenada por la última letra:")
print(resultado)
