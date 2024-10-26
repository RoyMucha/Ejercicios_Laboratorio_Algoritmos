def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 == 0:
        raise ValueError("No se puede dividir por cero.")
    return num1 / num2

def calculadora():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        operacion = input("Ingrese la operación (+, -, *, /): ").strip()

        if operacion == '+':
            resultado = sumar(num1, num2)
        elif operacion == '-':
            resultado = restar(num1, num2)
        elif operacion == '*':
            resultado = multiplicar(num1, num2)
        elif operacion == '/':
            resultado = dividir(num1, num2)
        else:
            print("Operación no válida. Por favor, use +, -, *, o /.")
            return

        print("El resultado es: {:.2f}".format(resultado))

    except ValueError as e:
        print("Entrada no válida:", e)

# Llamar a la función para realizar la calculadora
calculadora()
