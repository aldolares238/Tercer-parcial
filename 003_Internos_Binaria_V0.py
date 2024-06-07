#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: Inserción Binaria

import matplotlib.pyplot as plt
import numpy as np

# Función para encontrar el índice donde se debe insertar el valor utilizando búsqueda binaria
def binary_search(arr, val, start, end):
    # Si el valor es mayor que el valor del último índice, retorna el siguiente índice
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start + 1

    # Si el rango está vacío, retorna el índice de inicio
    if start > end:
        return start

    # Encuentra el punto medio del rango actual
    mid = (start + end) // 2

    # Compara el valor medio con el valor a insertar y ajusta los límites en consecuencia
    if arr[mid] < val:
        return binary_search(arr, val, mid + 1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid - 1)
    else:
        return mid

# Función para realizar la inserción binaria en una lista
def binary_insertion_sort(arr):
    # Itera sobre cada elemento del array empezando desde el segundo
    for i in range(1, len(arr)):
        val = arr[i]  # Valor actual a ser insertado
        j = binary_search(arr, val, 0, i - 1)  # Encuentra la posición correcta usando búsqueda binaria
        arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]  # Inserta el valor en la posición correcta
        # Muestra el progreso del ordenamiento
        plot_progress(arr, i)
    return arr

# Función para graficar el progreso del ordenamiento
def plot_progress(arr, step):
    plt.figure()
    plt.bar(range(len(arr)), arr, color='blue')
    plt.title(f'Paso {step}')
    plt.xlabel('Índice')
    plt.ylabel('Valor')
    plt.show()

# Lista de ejemplo
arr = np.random.randint(1, 100, 10).tolist()
print("Lista original:", arr)

# Ordena la lista usando inserción binaria y grafica cada paso
sorted_arr = binary_insertion_sort(arr)
print("Lista ordenada:", sorted_arr)


