# Ejemplo 1: Lista de números
list_num = [4, 2, 9, 1, 5,20,0.1 ,0.5 ,12,35]
nueva_lista = sorted(list_num)  # Crea una nueva lista ordenada
print(nueva_lista)  # Salida: [1, 2, 4, 5, 9]
print(list_num)      # La lista original permanece sin cambios: [4, 2, 9, 1, 5]


numeros_desc = sorted(list_num, reverse=True)
print(numeros_desc)  # Salida: [9, 5, 4, 2, 1]