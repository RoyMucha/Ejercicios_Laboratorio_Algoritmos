#Dada una lista de tuplas, donde cada tupla contiene el nombre y la edad de una persona, ordenar la lista por edad 
#usando sorted() y una función lambda como key.



# Lista de diccionarios con productos
productos = [
    {"nombre": "Laptop", "precio": 1200},
    {"nombre": "Teléfono", "precio": 800},
    {"nombre": "Tablet", "precio": 500},
    {"nombre": "Auriculares", "precio": 150}
]

# Ordenar la lista de productos por precio en orden descendente
productos.sort(key=lambda producto: producto["precio"], reverse=True)

# Mostrar la lista ordenada
print("Lista de productos ordenada por precio en orden descendente:")
for producto in productos:
    print("Nombre: {}, Precio: {}".format(producto["nombre"], producto["precio"]))
