import random
import string

def generar_contrasena(longitud, mayusculas=True, minusculas=True, numeros=True, especiales=True):
    if longitud <= 0:
        raise ValueError("La longitud de la contraseña debe ser mayor que 0.")
    
    caracteres = ""
    
    if mayusculas:
        caracteres += string.ascii_uppercase
    if minusculas:
        caracteres += string.ascii_lowercase
    if numeros:
        caracteres += string.digits
    if especiales:
        caracteres += string.punctuation
    
    if not caracteres:
        raise ValueError("Debes incluir al menos un tipo de carácter.")

    # Generar la contraseña aleatoria
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    
    return contrasena

def main():
    try:
        longitud = int(input("Ingrese la longitud de la contraseña: "))
        mayusculas = input("¿Incluir letras mayúsculas? (s/n): ").strip().lower() == 's'
        minusculas = input("¿Incluir letras minúsculas? (s/n): ").strip().lower() == 's'
        numeros = input("¿Incluir números? (s/n): ").strip().lower() == 's'
        especiales = input("¿Incluir caracteres especiales? (s/n): ").strip().lower() == 's'
        
        contrasena = generar_contrasena(longitud, mayusculas, minusculas, numeros, especiales)
        print("Contraseña generada:", contrasena)

    except ValueError as e:
        print("Error:", e)

# Llamar a la función principal
main()
