#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: Natural merging

# Importamos las bibliotecas necesarias
import random
import matplotlib.pyplot as plt

# Función para realizar el merge de dos sublistas ordenadas
def merge(left, right):
    # Lista que contendrá el resultado de la combinación
    merged = []
    # Índices para iterar sobre las listas left y right
    i = 0
    j = 0
    # Mientras haya elementos en ambas listas
    while i < len(left) and j < len(right):
        # Comparar y añadir el elemento menor a la lista merged
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    # Añadir los elementos restantes de left (si los hay)
    while i < len(left):
        merged.append(left[i])
        i += 1
    # Añadir los elementos restantes de right (si los hay)
    while j < len(right):
        merged.append(right[j])
        j += 1
    return merged

# Función para encontrar las subsecuencias naturales en la lista
def find_natural_sublists(lst):
    # Lista que contendrá las sublistas encontradas
    sublists = []
    # Sublista temporal
    temp_list = [lst[0]]
    # Iteramos sobre la lista para encontrar sublistas naturales
    for i in range(1, len(lst)):
        if lst[i] >= lst[i - 1]:
            temp_list.append(lst[i])
        else:
            sublists.append(temp_list)
            temp_list = [lst[i]]
    # Añadimos la última sublista
    sublists.append(temp_list)
    return sublists

# Función principal del algoritmo Natural Merging
def natural_merge_sort(lst):
    # Encontramos las sublistas naturales
    sublists = find_natural_sublists(lst)
    # Mientras haya más de una sublista, seguimos combinando
    while len(sublists) > 1:
        new_sublists = []
        for i in range(0, len(sublists), 2):
            if i + 1 < len(sublists):
                merged_list = merge(sublists[i], sublists[i + 1])
                new_sublists.append(merged_list)
            else:
                new_sublists.append(sublists[i])
        sublists = new_sublists
    return sublists[0]

# Generamos una lista aleatoria de números
random_list = [random.randint(0, 100) for _ in range(20)]
# Ordenamos la lista usando el algoritmo Natural Merging
sorted_list = natural_merge_sort(random_list)

# Mostramos los resultados
print("Lista Original:", random_list)
print("Lista Ordenada:", sorted_list)

# Función para mostrar las listas usando matplotlib
def plot_lists(original, sorted):
    # Creamos una figura y ejes
    fig, axs = plt.subplots(2, 1, figsize=(10, 8))
    
    # Graficamos la lista original
    axs[0].bar(range(len(original)), original, color='blue')
    axs[0].set_title('Lista Original')
    
    # Graficamos la lista ordenada
    axs[1].bar(range(len(sorted)), sorted, color='green')
    axs[1].set_title('Lista Ordenada')
    
    # Mostramos el gráfico
    plt.tight_layout()
    plt.show()

# Llamamos a la función para mostrar los gráficos
plot_lists(random_list, sorted_list)
