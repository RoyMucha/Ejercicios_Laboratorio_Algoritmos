import random

# Opciones
opciones = ["piedra", "papel", "tijera"]

# Solicitar la elección del usuario
eleccion_usuario = input("Elige 'piedra', 'papel' o 'tijera': ").lower()

# Verificar si la elección del usuario es válida
if eleccion_usuario not in opciones:
    print("Elección no válida. Por favor, elige 'piedra', 'papel' o 'tijera'.")
else:
    # Generar elección aleatoria para la computadora
    eleccion_computadora = random.choice(opciones)

    print("La computadora eligió:", eleccion_computadora)

    # Determinar el ganador
    if eleccion_usuario == eleccion_computadora:
        print("¡Es un empate!")
    elif (eleccion_usuario == "piedra" and eleccion_computadora == "tijera") or \
         (eleccion_usuario == "papel" and eleccion_computadora == "piedra") or \
         (eleccion_usuario == "tijera" and eleccion_computadora == "papel"):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")
