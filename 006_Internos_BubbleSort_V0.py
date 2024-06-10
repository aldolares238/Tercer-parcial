#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: BubbleSort

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation  # Importar el módulo animation

# Función de ordenamiento Burbuja (Bubble Sort)
def bubble_sort(arr):
    n = len(arr)  # Obtiene la longitud del arreglo
    for i in range(n):  # Recorre todo el arreglo
        for j in range(0, n-i-1):  # Recorre el arreglo desde el principio hasta el final menos el índice ya ordenado
            if arr[j] > arr[j+1]:  # Compara el elemento actual con el siguiente
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Intercambia los elementos si están en el orden incorrecto
                yield arr  # Devuelve el arreglo en su estado actual para la visualización

# Función para graficar el proceso de ordenamiento
def visualize_bubble_sort(arr):
    generator = bubble_sort(arr)  # Crea un generador a partir de la función bubble_sort
    fig, ax = plt.subplots()  # Crea una figura y un eje para la gráfica
    bar_rects = ax.bar(range(len(arr)), arr, align="edge")  # Dibuja las barras iniciales
    ax.set_xlim(0, len(arr))  # Establece los límites del eje x
    ax.set_ylim(0, int(1.1 * max(arr)))  # Establece los límites del eje y

    # Función para actualizar las barras en la gráfica
    def update_fig(arr, rects):
        for rect, val in zip(rects, arr):  # Recorre las barras y los valores del arreglo
            rect.set_height(val)  # Actualiza la altura de cada barra

    anim = animation.FuncAnimation(fig, func=update_fig,
                                   fargs=(bar_rects,), frames=generator, repeat=False, blit=False)  # Crea la animación
    plt.show()  # Muestra la gráfica

# Arreglo de ejemplo
arr = np.random.randint(1, 100, size=20)  # Crea un arreglo de 20 elementos con valores aleatorios entre 1 y 100

# Llamada a la función de visualización
visualize_bubble_sort(arr)
