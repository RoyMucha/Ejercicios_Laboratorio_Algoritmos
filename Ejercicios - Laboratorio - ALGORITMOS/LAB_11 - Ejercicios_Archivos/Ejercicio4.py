#"Contador de palabras": Desarrolla un programa que lea un archivo de texto y cuente la frecuencia de cada 
#palabra. Muestra las 10 palabras más frecuentes


# Solicitar el nombre del archivo
nombre_archivo = input("Ingresa el nombre del archivo de texto (incluye .txt): ")

# Inicializar un diccionario para contar las palabras
contador_palabras = {}

# Leer el archivo y contar las palabras
try:
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            # Dividir la línea en palabras
            palabras = linea.split()
            for palabra in palabras:
                # Convertir la palabra a minúsculas para un conteo uniforme
                palabra = palabra.lower().strip('.,!?";:()[]{}')  # Eliminar puntuaciones
                if palabra:  # Comprobar que no esté vacío
                    if palabra in contador_palabras:
                        contador_palabras[palabra] += 1
                    else:
                        contador_palabras[palabra] = 1

    # Ordenar las palabras por frecuencia
    palabras_frecuentes = sorted(contador_palabras.items(), key=lambda x: x[1], reverse=True)

    # Mostrar las 10 palabras más frecuentes
    print("Las 10 palabras más frecuentes son:")
    for i in range(min(10, len(palabras_frecuentes))):  # Asegurar que no exceda el número de palabras
        palabra, frecuencia = palabras_frecuentes[i]
        print("Palabra: " + palabra + ", Frecuencia: " + str(frecuencia))

except FileNotFoundError:
    print("El archivo no se encontró.")