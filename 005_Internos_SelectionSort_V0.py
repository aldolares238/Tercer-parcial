#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: SelectionSort

import matplotlib.pyplot as plt  # Importamos la librería matplotlib para la visualización
import numpy as np  # Importamos la librería numpy para generar datos de prueba
from matplotlib.animation import FuncAnimation  # Importamos FuncAnimation para animaciones

def selection_sort(arr):
    """Función que implementa el algoritmo de ordenamiento por selección"""
    n = len(arr)  # Obtenemos la longitud del array
    for i in range(n):
        min_idx = i  # Inicializamos el índice del valor mínimo como el índice actual
        for j in range(i+1, n):
            # Si encontramos un valor menor, actualizamos el índice del mínimo
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Intercambiamos el valor mínimo encontrado con el valor en la posición i
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        yield arr, i, min_idx  # Usamos yield para generar el array en cada paso

def visualize_selection_sort(arr):
    """Función para visualizar el algoritmo de ordenamiento por selección"""
    fig, ax = plt.subplots()  # Creamos una figura y un eje para el gráfico
    bar_rects = ax.bar(range(len(arr)), arr, align="edge")  # Creamos las barras iniciales

    ax.set_xlim(0, len(arr))  # Establecemos los límites del eje x
    ax.set_ylim(0, int(1.1 * max(arr)))  # Establecemos los límites del eje y

    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)  # Añadimos un texto para mostrar el paso actual
    iteration = [0]  # Lista para almacenar el número de iteraciones

    def update(selection_data):
        """Función para actualizar el gráfico en cada paso"""
        arr, i, min_idx = selection_data  # Desempaquetamos los datos de selección
        for rect, val in zip(bar_rects, arr):
            rect.set_height(val)  # Actualizamos la altura de cada barra
        iteration[0] += 1  # Incrementamos el número de iteraciones
        text.set_text(f"Paso: {iteration[0]}, i={i}, min_idx={min_idx}")  # Actualizamos el texto del paso actual

    # Llamamos a la función de ordenamiento y actualizamos el gráfico en cada paso
    anim = FuncAnimation(fig, func=update, frames=selection_sort(arr), repeat=False)
    plt.show()  # Mostramos el gráfico

# Generamos un array de prueba de 10 elementos con valores aleatorios
arr = np.random.randint(0, 100, size=10)
visualize_selection_sort(arr)  # Llamamos a la función para visualizar el ordenamiento
