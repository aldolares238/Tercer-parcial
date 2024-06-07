#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: ShellSort

import matplotlib.pyplot as plt  # Importa la librería matplotlib para generar gráficos
import numpy as np  # Importa numpy para manejar arrays de manera más eficiente

def shell_sort(arr):
    n = len(arr)  # Obtiene el tamaño del array
    gap = n // 2  # Inicializa el intervalo (gap) a la mitad del tamaño del array

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]  # Guarda el valor actual en la posición i
            j = i  # Inicializa j con el valor de i

            # Realiza el intercambio de elementos mientras se cumple la condición
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]  # Mueve el elemento a la posición j
                j -= gap  # Reduce el índice j en el valor del intervalo (gap)

            arr[j] = temp  # Coloca el valor guardado en su posición correcta
        gap //= 2  # Reduce el intervalo (gap) a la mitad

    return arr  # Retorna el array ordenado

def plot_sorting_process(arr):
    # Crea una figura y un conjunto de ejes
    fig, ax = plt.subplots()

    # Grafica el array desordenado
    ax.bar(range(len(arr)), arr, align='center', color='blue')
    ax.set_title('Array desordenado')
    plt.show()

    n = len(arr)  # Obtiene el tamaño del array
    gap = n // 2  # Inicializa el intervalo (gap) a la mitad del tamaño del array

    iteration = 0  # Contador de iteraciones

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]  # Guarda el valor actual en la posición i
            j = i  # Inicializa j con el valor de i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]  # Mueve el elemento a la posición j
                j -= gap  # Reduce el índice j en el valor del intervalo (gap)

            arr[j] = temp  # Coloca el valor guardado en su posición correcta

            # Grafica el array en cada iteración
            fig, ax = plt.subplots()
            ax.bar(range(len(arr)), arr, align='center', color='blue')
            ax.set_title(f'Iteración {iteration}, gap {gap}')
            plt.show()

            iteration += 1  # Incrementa el contador de iteraciones

        gap //= 2  # Reduce el intervalo (gap) a la mitad

    return arr  # Retorna el array ordenado

# Array de ejemplo para ordenar
array_to_sort = np.random.randint(1, 100, 20)  # Genera un array de 20 elementos con valores aleatorios entre 1 y 100

# Muestra el array desordenado
print("Array desordenado:", array_to_sort)

# Llama a la función para ordenar el array y mostrar el proceso
sorted_array = plot_sorting_process(array_to_sort)

# Muestra el array ordenado
print("Array ordenado:", sorted_array)
