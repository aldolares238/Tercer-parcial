#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: Balanced multiway merging

import matplotlib.pyplot as plt
import heapq

# Función que realiza el algoritmo de Balanced Multiway Merging
def balanced_multiway_merge(lists):
    # Crear un heap que almacenará los elementos más pequeños de cada lista
    heap = []
    # Insertar el primer elemento de cada lista junto con el índice de la lista y el índice del elemento
    for i, lst in enumerate(lists):
        if lst:  # Verificar que la lista no esté vacía
            heapq.heappush(heap, (lst[0], i, 0))

    # Lista para almacenar el resultado de la fusión
    merged_list = []
    # Mientras el heap no esté vacío
    while heap:
        # Obtener el elemento más pequeño del heap
        val, list_idx, element_idx = heapq.heappop(heap)
        # Agregar el elemento más pequeño al resultado de la fusión
        merged_list.append(val)
        # Si el elemento extraído no es el último de su lista original
        if element_idx + 1 < len(lists[list_idx]):
            # Insertar el siguiente elemento de la misma lista al heap
            next_val = lists[list_idx][element_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, element_idx + 1))

    return merged_list

# Listas de ejemplo para fusionar
lists = [
    [1, 5, 9],
    [2, 6, 10],
    [3, 7, 11],
    [4, 8, 12]
]

# Llamar a la función de fusión
result = balanced_multiway_merge(lists)

# Imprimir el resultado de la fusión
print("Merged List:", result)

# Graficar el resultado
# Crear una figura y un eje
fig, ax = plt.subplots()

# Título del gráfico
ax.set_title('Balanced Multiway Merging')

# Etiquetas de los ejes
ax.set_xlabel('Index')
ax.set_ylabel('Value')

# Dibujar los valores fusionados
ax.plot(result, 'o-', label='Merged List')

# Dibujar las listas originales para comparación
for i, lst in enumerate(lists):
    ax.plot(lst, 'x--', label=f'List {i+1}')

# Mostrar leyenda
ax.legend()

# Mostrar la gráfica
plt.show()
