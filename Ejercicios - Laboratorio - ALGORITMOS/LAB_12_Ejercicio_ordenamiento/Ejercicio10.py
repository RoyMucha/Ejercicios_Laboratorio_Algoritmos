#Ordenar una lista de tuplas, donde cada tupla contiene (nombre, edad, ciudad), primero por ciudad en orden 
#alfabético, luego por edad en orden descendente y finalmente por nombre en orden alfabético, usando sorted() y 
#una función lambda como key.

# Lista de tuplas (nombre, edad, ciudad)
personas = [
    ("Juan", 25, "Madrid"),
    ("Ana", 22, "Barcelona"),
    ("Pedro", 30, "Madrid"),
    ("María", 22, "Barcelona"),
    ("Luis", 35, "Valencia"),
    ("Sofia", 28, "Madrid"),
]

# Ordenar la lista por ciudad, edad (descendente) y nombre
personas_ordenadas = sorted(personas, key=lambda persona: (persona[2], -persona[1], persona[0]))

# Mostrar la lista ordenada
print("Lista de personas ordenada:")
for persona in personas_ordenadas:
    print("Nombre:", persona[0], ", Edad:", persona[1], ", Ciudad:", persona[2])
