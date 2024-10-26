def bubble_sort(lista):
    n = len(lista)   
    for i in range(n):    #  n=5 ;    i=0 , i=1, i=2 , i=3, i=4
        # Bandera para verificar si hubo algún intercambio
        intercambio = False
        for j in range(0,n-i-1):  #     j=0, j=1 , j=2, j=3
            # Si el elemento actual es mayor que el siguiente, intercambiamos
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                intercambio = True
        # Si no hubo intercambio en una pasada, la lista está ordenada
        if not intercambio:
            break

# Ejemplo de uso
lista = [5, 1, 4, 2, 8]
bubble_sort(lista)
print("Lista ordenada:", lista)  # Salida: [1, 2, 4, 5, 8]
