#"Organizador de archivos": Crea un script que organice archivos en una carpeta. Por ejemplo, mover todas las 
#imágenes a una carpeta "Imágenes", los documentos de texto a una carpeta "Documentos", etc.


import os
import shutil

# Función para organizar archivos en una carpeta
def organizar_archivos(carpeta):
    # Crear carpetas para imágenes y documentos si no existen
    carpeta_imagenes = os.path.join(carpeta, "Imágenes")
    carpeta_documentos = os.path.join(carpeta, "Documentos")
    
    if not os.path.exists(carpeta_imagenes):
        os.makedirs(carpeta_imagenes)
        
    if not os.path.exists(carpeta_documentos):
        os.makedirs(carpeta_documentos)

    # Listar todos los archivos en la carpeta especificada
    for archivo in os.listdir(carpeta):
        ruta_archivo = os.path.join(carpeta, archivo)
        
        # Comprobar si es un archivo y no una carpeta
        if os.path.isfile(ruta_archivo):
            # Mover archivos de imagen
            if archivo.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                shutil.move(ruta_archivo, carpeta_imagenes)
                print("Moviendo imagen: " + archivo + " a " + carpeta_imagenes)
            # Mover documentos de texto
            elif archivo.lower().endswith(('.txt', '.doc', '.docx', '.pdf')):
                shutil.move(ruta_archivo, carpeta_documentos)
                print("Moviendo documento: " + archivo + " a " + carpeta_documentos)

# Solicitar la carpeta a organizar
carpeta_a_organizar = input("Ingresa la ruta de la carpeta que deseas organizar: ")
organizar_archivos(carpeta_a_organizar)