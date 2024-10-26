#"Procesador de texto simple": Crea un programa que permita al usuario abrir un archivo de texto (.txt), 
#escribir nuevo texto al final del archivo y guardarlo.


# Solicitar al usuario el nombre del archivo
archivo_nombre = input("Ingresa el nombre del archivo de texto (incluye .txt): ")

try:
    # Intentar abrir el archivo en modo de lectura para verificar que existe
    with open(archivo_nombre, 'r') as archivo:
        print("Contenido actual del archivo:")
        print(archivo.read())
except FileNotFoundError:
    print("El archivo no existe. Se creará uno nuevo.")

# Solicitar al usuario el texto que desea agregar
nuevo_texto = input("Escribe el texto que deseas agregar al archivo: ")

# Abrir el archivo en modo de agregado para escribir el nuevo texto al final
with open(archivo_nombre, 'a') as archivo:
    archivo.write(nuevo_texto + "\n")

print("El texto ha sido agregado y el archivo guardado correctamente.")