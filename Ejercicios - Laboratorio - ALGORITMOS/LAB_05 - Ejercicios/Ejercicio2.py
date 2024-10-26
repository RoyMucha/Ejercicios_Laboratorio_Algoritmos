# Frase dada
frase = "Soy profesor y me encanta inspirar y enseñar a la gente."

# Eliminar el punto al final y dividir la frase en palabras
palabras = frase[:-1].split()

# Usar un conjunto para obtener palabras únicas
palabras_unicas = set(palabras)

# Contar el número de palabras únicas
numero_palabras_unicas = len(palabras_unicas)

# Imprimir el resultado
print("Número de palabras únicas:", numero_palabras_unicas)
