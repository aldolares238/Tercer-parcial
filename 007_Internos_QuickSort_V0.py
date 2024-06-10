#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: QuickSort

# Importar las bibliotecas necesarias
import matplotlib.pyplot as plt
import numpy as np

# Función QuickSort
def quicksort(arr):
    # Si el array tiene 1 o 0 elementos, ya está ordenado
    if len(arr) <= 1:
        return arr
    else:
        # Selecciona el pivote, en este caso el elemento del medio
        pivot = arr[len(arr) // 2]
        # Crea subarrays: menos que el pivote, igual al pivote y mayor que el pivote
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        # Recursivamente aplica QuickSort a los subarrays izquierdo y derecho, y luego los combina
        return quicksort(left) + middle + quicksort(right)

# Crear un array aleatorio de 10 elementos
np.random.seed(0)  # Fijar la semilla para reproducibilidad
arr = np.random.randint(1, 100, 10)

# Imprimir el array original
print("Array original:", arr)

# Ordenar el array usando QuickSort
sorted_arr = quicksort(arr)

# Imprimir el array ordenado
print("Array ordenado:", sorted_arr)

# Configurar la gráfica
fig, ax = plt.subplots()

# Crear la gráfica de barras del array original
ax.bar(range(len(arr)), arr, color='blue', alpha=0.6, label='Original')

# Crear la gráfica de barras del array ordenado
ax.bar(range(len(sorted_arr)), sorted_arr, color='green', alpha=0.6, label='Ordenado')

# Añadir títulos y etiquetas
ax.set_title('QuickSort: Array Original vs. Array Ordenado')
ax.set_xlabel('Índice')
ax.set_ylabel('Valor')
ax.legend()

# Mostrar la gráfica
plt.show()
