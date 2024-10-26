#"Buscador de palabras": Crea un script que busque una palabra específica dentro de un archivo de texto y 
#muestre todas las líneas donde aparece la palabra, junto con el número de línea.



# Solicitar el nombre del archivo y la palabra a buscar
nombre_archivo = input("Ingresa el nombre del archivo de texto (incluye .txt): ")
palabra_buscada = input("Ingresa la palabra a buscar: ")

# Inicializar una lista para almacenar las líneas donde aparece la palabra
lineas_encontradas = []

# Leer el archivo y buscar la palabra
try:
    with open(nombre_archivo, 'r') as archivo:
        for numero_linea, linea in enumerate(archivo, start=1):
            if palabra_buscada in linea:
                lineas_encontradas.append((numero_linea, linea.strip()))

    # Mostrar los resultados
    if lineas_encontradas:
        print("Líneas donde aparece la palabra '" + palabra_buscada + "':")
        for numero_linea, linea in lineas_encontradas:
            print("Línea " + str(numero_linea) + ": " + linea)
    else:
        print("La palabra '" + palabra_buscada + "' no se encontró en el archivo.")

except FileNotFoundError:
    print("El archivo no se encontró.")
