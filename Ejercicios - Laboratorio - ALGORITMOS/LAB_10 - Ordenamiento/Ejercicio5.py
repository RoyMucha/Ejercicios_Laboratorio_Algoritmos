# Ejemplo: Ordenar por longitud de la cadena
list_frutas = ["mango", "uva", "platano", "pera", "cereza", "durazno","sandia"]
list_frutas.sort(key=lambda x: len(x))  # Ordena por longitud de cadena
print(list_frutas)  # Salida: ['pera', 'banana', 'manzana', 'naranja']

# Ejemplo: Ordenar por longitud en orden descendente
list_ordenadas = sorted(list_frutas, key=lambda x: len(x), reverse=True)
print(list_ordenadas)  # Salida: ['naranja', 'manzana', 'banana', 'pera']