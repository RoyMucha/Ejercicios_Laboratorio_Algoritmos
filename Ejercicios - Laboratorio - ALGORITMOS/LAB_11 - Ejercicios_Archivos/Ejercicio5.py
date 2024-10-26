#"Copiadora de archivos": Escribe un programa que copie el contenido de un archivo a otro archivo.

# Solicitar el nombre del archivo de origen y el archivo de destino
archivo_origen = input("Ingresa el nombre del archivo de origen (incluye .txt): ")
archivo_destino = input("Ingresa el nombre del archivo de destino (incluye .txt): ")

try:
    # Abrir el archivo de origen en modo lectura
    with open(archivo_origen, 'r') as origen:
        # Leer el contenido del archivo de origen
        contenido = origen.read()

    # Abrir el archivo de destino en modo escritura
    with open(archivo_destino, 'w') as destino:
        # Escribir el contenido en el archivo de destino
        destino.write(contenido)

    print("El contenido se ha copiado de " + archivo_origen + " a " + archivo_destino + ".")

except FileNotFoundError:
    print("El archivo de origen no se encontró.")