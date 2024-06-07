#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: InsertionSort

import matplotlib.pyplot as plt
import numpy as np

def insertion_sort(arr):
    # Comienza a recorrer el array desde el segundo elemento
    for i in range(1, len(arr)):
        # Almacena el valor actual en la variable key
        key = arr[i]
        # Inicializa j con el índice del elemento anterior
        j = i - 1
        # Mueve los elementos del array que son mayores que key una posición hacia adelante
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        # Coloca el valor key en su posición correcta
        arr[j + 1] = key

# Función para graficar el estado actual del array
def plot_array(arr, title):
    plt.figure(figsize=(10, 6))  # Define el tamaño de la figura
    plt.bar(range(len(arr)), arr, color='blue')  # Crea un gráfico de barras
    plt.title(title)  # Establece el título del gráfico
    plt.xlabel('Índice')  # Establece la etiqueta del eje X
    plt.ylabel('Valor')  # Establece la etiqueta del eje Y
    plt.show()  # Muestra el gráfico

# Define un array de ejemplo
array = [12, 11, 13, 5, 6]

# Muestra el array original
plot_array(array, 'Array Original')

# Ordena el array usando InsertionSort y muestra el progreso
for i in range(1, len(array)):
    # Almacena el valor actual en la variable key
    key = array[i]
    # Inicializa j con el índice del elemento anterior
    j = i - 1
    # Mueve los elementos del array que son mayores que key una posición hacia adelante
    while j >= 0 and key < array[j]:
        array[j + 1] = array[j]
        j -= 1
    # Coloca el valor key en su posición correcta
    array[j + 1] = key
    # Muestra el array después de cada inserción
    plot_array(array, f'Array después de insertar el elemento en la posición {i}')

# Muestra el array ordenado
plot_array(array, 'Array Ordenado')

