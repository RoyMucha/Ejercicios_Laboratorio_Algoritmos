#Dada una lista de objetos "Estudiante" con atributos "nombre" y "calificación", ordenar la lista por la longitud del 
#nombre en orden descendente usando sort(), una función lambda como key y reverse=True

class Estudiante:
    def __init__(self, nombre, calificacion):
        self.nombre = nombre
        self.calificacion = calificacion

# Lista de objetos Estudiante
estudiantes = [
    Estudiante("Juan", 85),
    Estudiante("María", 90),
    Estudiante("Pedro", 75),
    Estudiante("Ana", 95),
    Estudiante("Luis Alberto", 80),
]

# Ordenar la lista de estudiantes por la longitud del nombre en orden descendente
estudiantes.sort(key=lambda estudiante: len(estudiante.nombre), reverse=True)

# Mostrar la lista ordenada
print("Lista de estudiantes ordenada por la longitud del nombre (descendente):")
for estudiante in estudiantes:
    print("Nombre:", estudiante.nombre, ", Calificación:", estudiante.calificacion)

