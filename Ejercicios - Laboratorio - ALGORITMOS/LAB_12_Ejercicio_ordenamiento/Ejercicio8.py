#Crear una función que tome una lista de fechas en formato "dd/mm/aaaa" y las ordene por año usando sorted() 
#y una función lambda como key.

def ordenar_fechas(fechas):
    # Ordenar la lista de fechas por año usando sorted() y una función lambda
    fechas_ordenadas = sorted(fechas, key=lambda fecha: fecha.split("/")[2])
    return fechas_ordenadas

# Lista de fechas
lista_fechas = ["15/03/2023", "01/01/2022", "22/11/2023", "05/05/2021", "10/10/2022"]

# Llamar a la función y mostrar el resultado
resultado = ordenar_fechas(lista_fechas)
print("Lista de fechas ordenada por año:")
print(resultado)
