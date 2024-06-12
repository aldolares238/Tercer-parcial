#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: Straight merging

import matplotlib.pyplot as plt
import numpy as np

def merge(left, right):
    """Fusiona dos listas ordenadas en una sola lista ordenada."""
    result = []  # Lista resultado que contendrá los elementos fusionados
    i = 0  # Índice para la lista izquierda
    j = 0  # Índice para la lista derecha
    # Mientras haya elementos en ambas listas
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])  # Añade el elemento menor de la izquierda
            i += 1  # Incrementa el índice de la izquierda
        else:
            result.append(right[j])  # Añade el elemento menor de la derecha
            j += 1  # Incrementa el índice de la derecha
    # Añade los elementos restantes de la lista izquierda, si los hay
    result.extend(left[i:])
    # Añade los elementos restantes de la lista derecha, si los hay
    result.extend(right[j:])
    return result  # Devuelve la lista fusionada y ordenada

def straight_merge_sort(arr):
    """Ordena una lista usando el algoritmo de Straight Merging."""
    width = 1  # Comienza con bloques de tamaño 1
    n = len(arr)  # Longitud de la lista a ordenar
    while width < n:
        i = 0  # Índice inicial para el recorrido de la lista
        while i < n:
            left = arr[i:i+width]  # Sublista izquierda de tamaño 'width'
            right = arr[i+width:i+2*width]  # Sublista derecha de tamaño 'width'
            arr[i:i+2*width] = merge(left, right)  # Fusiona y asigna a la lista original
            i += 2 * width  # Avanza al siguiente bloque
        width *= 2  # Duplica el tamaño del bloque
    return arr  # Devuelve la lista ordenada

def plot_sorting_process(arr):
    """Muestra el proceso de ordenamiento gráficamente."""
    fig, ax = plt.subplots()  # Crea una figura y un eje
    bars = ax.bar(range(len(arr)), arr, align='center')  # Crea un gráfico de barras

    def update_bars(data, color='blue'):
        """Actualiza las barras del gráfico."""
        for bar, val in zip(bars, data):
            bar.set_height(val)  # Establece la altura de la barra
            bar.set_color(color)  # Establece el color de la barra
        plt.pause(0.1)  # Pausa para mostrar la actualización

    width = 1  # Comienza con bloques de tamaño 1
    n = len(arr)  # Longitud de la lista a ordenar
    while width < n:
        i = 0  # Índice inicial para el recorrido de la lista
        while i < n:
            left = arr[i:i+width]  # Sublista izquierda de tamaño 'width'
            right = arr[i+width:i+2*width]  # Sublista derecha de tamaño 'width'
            arr[i:i+2*width] = merge(left, right)  # Fusiona y asigna a la lista original
            update_bars(arr)  # Actualiza el gráfico con la lista fusionada
            i += 2 * width  # Avanza al siguiente bloque
        width *= 2  # Duplica el tamaño del bloque

    update_bars(arr, color='green')  # Actualiza el gráfico con la lista ordenada en verde
    plt.show()  # Muestra el gráfico

# Lista desordenada de ejemplo
unsorted_list = [34, 7, 23, 32, 5, 62, 78, 9, 1, 10, 4, 15, 22]

# Muestra el proceso de ordenamiento
plot_sorting_process(unsorted_list)
