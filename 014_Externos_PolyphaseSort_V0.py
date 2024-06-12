#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: Polyphase sort

import matplotlib.pyplot as plt  # Importamos matplotlib para la visualización
import random  # Importamos random para generar datos aleatorios

def generate_random_data(size):
    """Genera una lista de datos aleatorios."""
    return [random.randint(0, 100) for _ in range(size)]

def polyphase_sort(data):
    """
    Realiza el algoritmo de ordenación poliédrica.
    Paso 1: Divide los datos en particiones.
    Paso 2: Ordena internamente cada partición.
    Paso 3: Fusiona las particiones ordenadas en un solo archivo.
    """
    # Paso 1: Divide los datos en particiones (usaremos 3 particiones como ejemplo)
    partition_size = len(data) // 3
    partitions = [data[i * partition_size:(i + 1) * partition_size] for i in range(3)]
    
    # Si hay elementos restantes, los añadimos a la última partición
    if len(data) % 3 != 0:
        partitions[-1].extend(data[3 * partition_size:])

    # Paso 2: Ordena internamente cada partición
    for i in range(len(partitions)):
        partitions[i].sort()

    # Paso 3: Fusiona las particiones ordenadas
    sorted_data = []
    while any(partitions):
        # Encuentra el menor elemento entre las particiones
        min_values = [partition[0] for partition in partitions if partition]
        min_value = min(min_values)
        for partition in partitions:
            if partition and partition[0] == min_value:
                sorted_data.append(partition.pop(0))
                break

    return sorted_data

def plot_data(data, sorted_data):
    """Muestra los datos originales y ordenados de manera gráfica."""
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.plot(data, 'o-')
    plt.title('Datos Originales')
    plt.xlabel('Índice')
    plt.ylabel('Valor')

    plt.subplot(1, 2, 2)
    plt.plot(sorted_data, 'o-')
    plt.title('Datos Ordenados (Polyphase Sort)')
    plt.xlabel('Índice')
    plt.ylabel('Valor')

    plt.tight_layout()
    plt.show()

def main():
    """Función principal para ejecutar el script."""
    data_size = 30  # Tamaño de los datos aleatorios
    data = generate_random_data(data_size)  # Genera los datos aleatorios
    print("Datos Originales:", data)  # Imprime los datos originales

    sorted_data = polyphase_sort(data)  # Ordena los datos usando polyphase sort
    print("Datos Ordenados:", sorted_data)  # Imprime los datos ordenados

    plot_data(data, sorted_data)  # Muestra los datos de manera gráfica

if __name__ == "__main__":
    main()  # Ejecuta el script
