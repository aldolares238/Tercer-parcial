#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: MergeSort


import matplotlib.pyplot as plt
import numpy as np

# Función para realizar el MergeSort
def merge_sort(arr, depth=0):
    # Si la longitud del arreglo es menor o igual a 1, ya está ordenado
    if len(arr) <= 1:
        return arr

    # Encontrar el punto medio del arreglo
    mid = len(arr) // 2

    # Dividir el arreglo en dos mitades
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Llamada recursiva para ordenar cada mitad
    sorted_left = merge_sort(left_half, depth + 1)
    sorted_right = merge_sort(right_half, depth + 1)

    # Mezclar las dos mitades ordenadas
    return merge(sorted_left, sorted_right)

# Función para mezclar dos arreglos ordenados
def merge(left, right):
    result = []  # Arreglo resultante
    i = j = 0

    # Comparar los elementos de los dos arreglos y añadir el menor al resultado
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Añadir los elementos restantes de cada arreglo (si los hay)
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Función para visualizar el proceso de MergeSort
def visualize_merge_sort(arr):
    fig, ax = plt.subplots()  # Crear la figura y los ejes
    bars = ax.bar(range(len(arr)), arr)  # Crear las barras iniciales

    def update_bars(arr, bars):
        for bar, val in zip(bars, arr):
            bar.set_height(val)  # Actualizar la altura de cada barra
        plt.pause(0.1)  # Pausar para permitir la visualización

    # Función recursiva para actualizar la visualización en cada paso del MergeSort
    def merge_sort_visual(arr, depth=0):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        sorted_left = merge_sort_visual(left_half, depth + 1)
        sorted_right = merge_sort_visual(right_half, depth + 1)

        merged = merge(sorted_left, sorted_right)
        
        # Mostrar el proceso de mezcla
        if depth == 0:
            update_bars(merged, bars)
        return merged

    merge_sort_visual(arr)  # Llamar a la función visualizada
    plt.show()  # Mostrar la gráfica final

# Crear un arreglo aleatorio para ordenar
np.random.seed(42)  # Semilla para reproducibilidad
arr = np.random.randint(1, 100, 20)

# Imprimir el arreglo original
print("Arreglo original:", arr)

# Visualizar el proceso de ordenamiento
visualize_merge_sort(arr)

# Ordenar el arreglo utilizando MergeSort
sorted_arr = merge_sort(arr)

# Imprimir el arreglo ordenado
print("Arreglo ordenado:", sorted_arr)
