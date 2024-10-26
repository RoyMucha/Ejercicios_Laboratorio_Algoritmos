#Dada una lista de diccionarios, donde cada diccionario representa un producto con "nombre" y "precio", ordena 
#la lista por precio usando Insertion Sort y luego por nombre en orden alfabético inverso

# Lista de diccionarios que representan productos
productos = [
    {"nombre": "manzana", "precio": 1.2},
    {"nombre": "banana", "precio": 0.8},
    {"nombre": "naranja", "precio": 1.0},
    {"nombre": "kiwi", "precio": 2.5},
    {"nombre": "cereza", "precio": 3.0},
    {"nombre": "aguacate", "precio": 2.0},
]

print("Lista original:")
print(productos)

# Implementación de Insertion Sort para ordenar por precio y luego por nombre
def insertion_sort_productos(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        
        # Comparar primero por precio y luego por nombre
        while j >= 0 and (lista[j]["precio"] > clave["precio"] or 
                          (lista[j]["precio"] == clave["precio"] and lista[j]["nombre"] < clave["nombre"])):
            lista[j + 1] = lista[j]
            j -= 1
            
        # Insertar el producto en la posición correcta
        lista[j + 1] = clave

# Ordenar la lista usando Insertion Sort
insertion_sort_productos(productos)

print("Lista ordenada por precio y luego por nombre en orden alfabético inverso:")
print(productos)
