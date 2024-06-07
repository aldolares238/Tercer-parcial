#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: Hashing

import matplotlib.pyplot as plt

# Definimos el tamaño de la tabla hash
TABLE_SIZE = 10

# Función hash simple
def simple_hash(key):
    # Calculamos el índice de la tabla hash usando el residuo de la división
    return key % TABLE_SIZE

# Función para insertar una clave en la tabla hash
def insert(table, key):
    # Calculamos la posición usando la función hash
    index = simple_hash(key)
    
    # Colisión: si la posición ya está ocupada
    while table[index] is not None:
        # Movemos al siguiente índice (linealmente)
        index = (index + 1) % TABLE_SIZE
    
    # Insertamos la clave en la posición calculada
    table[index] = key

# Visualización de la tabla hash
def visualize_hash_table(table):
    # Configuramos la figura y el tamaño
    plt.figure(figsize=(10, 2))
    plt.title("Tabla Hash")
    
    # Dibujamos las casillas de la tabla
    for i in range(TABLE_SIZE):
        plt.text(i, 0, str(table[i]), ha='center', va='center', bbox=dict(facecolor='white', edgecolor='black'))
    
    # Configuramos el eje X
    plt.xlim(-0.5, TABLE_SIZE - 0.5)
    plt.xticks(range(TABLE_SIZE))
    
    # Ocultamos el eje Y
    plt.yticks([])
    
    # Mostramos la cuadrícula y la tabla hash
    plt.grid(True)
    plt.show()

# Lista de claves a insertar
keys = [23, 43, 1, 87, 92, 33]

# Inicializamos la tabla hash con None (vacía)
hash_table = [None] * TABLE_SIZE

# Insertamos cada clave en la tabla hash
for key in keys:
    insert(hash_table, key)

# Mostramos el contenido de la tabla hash
print("Contenido de la tabla hash:")
for i, value in enumerate(hash_table):
    print(f"Índice {i}: {value}")

# Visualizamos la tabla hash
visualize_hash_table(hash_table)
