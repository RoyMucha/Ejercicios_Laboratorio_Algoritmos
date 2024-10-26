#Dada una lista de tuplas, donde cada tupla contiene el nombre y la edad de una persona, ordenar la lista por edad 
#usando sorted() y una función lambda como key.


# Lista de tuplas con nombre y edad
lista_personas = [("Juan", 25), ("María", 22), ("Pedro", 30), ("Ana", 28)]

# Ordenar la lista por edad utilizando sorted() y una función lambda
lista_ordenada = sorted(lista_personas, key=lambda persona: persona[1])

# Mostrar la lista ordenada
print("Lista ordenada por edad:")
for persona in lista_ordenada:
    print(persona)
