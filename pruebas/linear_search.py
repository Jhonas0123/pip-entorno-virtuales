# performing a linear search in O(n)

import random

def busqueda_lineal(lista, objetivo):
    match = False
    for elemento in lista: # O(n)
        if elemento == objetivo:
            match = True
            break
    return match

if __name__ == '__main__':
    # Solicitar tamaño de la lista al usuario
    tamaño_lista = int(input("¿De qué tamaño será la lista? "))
    
    # Solicitar el objetivo que desea encontrar
    objetivo = int(input("¿Qué número quieres encontrar? "))
    
    # Generar lista de números aleatorios
    lista = [random.randint(0, 100) for _ in range(tamaño_lista)]
    print("Lista:", lista)
    
    # Buscar objetivo en la lista
    encontrado = busqueda_lineal(lista, objetivo)
    
    # Imprimir resultado
    print(f"El elemento {objetivo} {'está' if encontrado else 'no está'} en la lista")