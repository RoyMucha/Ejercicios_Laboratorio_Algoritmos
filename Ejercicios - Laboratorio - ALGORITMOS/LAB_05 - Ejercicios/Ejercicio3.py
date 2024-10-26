
lista1 = list(range(1, 11))  
lista2 = list(range(5, 16))  
lista3 = list(range(10, 21))  


conjunto1 = set(lista1)
conjunto2 = set(lista2)
conjunto3 = set(lista3)

conjunto_interseccion = conjunto1.intersection(conjunto2).intersection(conjunto3)

conjunto_union = conjunto1.union(conjunto2).union(conjunto3)

conjunto_diferencia = conjunto1.difference(conjunto3)

tupla_interseccion = tuple(conjunto_interseccion)
tupla_union = tuple(conjunto_union)
tupla_diferencia = tuple(conjunto_diferencia)

suma_interseccion = tupla_interseccion[0] + tupla_interseccion[-1] if tupla_interseccion else 0
suma_union = tupla_union[0] + tupla_union[-1] if tupla_union else 0
suma_diferencia = tupla_diferencia[0] + tupla_diferencia[-1] if tupla_diferencia else 0

print("Conjunto de intersección:", conjunto_interseccion)
print("Conjunto de unión:", conjunto_union)
print("Conjunto de diferencia (lista1 - lista3):", conjunto_diferencia)
print("Suma de primer y último elemento de la tupla de intersección:", suma_interseccion)
print("Suma de primer y último elemento de la tupla de unión:", suma_union)
print("Suma de primer y último elemento de la tupla de diferencia:", suma_diferencia)
