#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: Ordenamiento de árbol.

import matplotlib.pyplot as plt  # Importamos la librería matplotlib para la visualización gráfica

# Definimos una clase para el nodo del árbol binario de búsqueda
class TreeNode:
    def __init__(self, key):
        self.left = None  # Hijo izquierdo
        self.right = None  # Hijo derecho
        self.val = key  # Valor del nodo

# Función para insertar un nuevo nodo en el árbol binario de búsqueda
def insert(root, key):
    # Si el árbol está vacío, devolvemos un nuevo nodo
    if root is None:
        return TreeNode(key)
    
    # De lo contrario, recorremos el árbol
    if key < root.val:
        root.left = insert(root.left, key)  # Insertamos en el subárbol izquierdo
    else:
        root.right = insert(root.right, key)  # Insertamos en el subárbol derecho
    
    return root

# Función para realizar el recorrido en orden del árbol binario de búsqueda y almacenar los valores ordenados
def inorder_traversal(root, res):
    if root:
        inorder_traversal(root.left, res)  # Recorremos el subárbol izquierdo
        res.append(root.val)  # Visitamos el nodo raíz
        inorder_traversal(root.right, res)  # Recorremos el subárbol derecho

# Función para realizar el ordenamiento utilizando el árbol binario de búsqueda
def tree_sort(arr):
    if len(arr) == 0:
        return []
    
    root = None  # Inicializamos la raíz del árbol
    for key in arr:
        root = insert(root, key)  # Insertamos cada clave en el árbol
    
    sorted_arr = []
    inorder_traversal(root, sorted_arr)  # Realizamos el recorrido en orden para obtener los elementos ordenados
    return sorted_arr

# Función para graficar el proceso de ordenamiento
def plot_sorting(arr):
    plt.figure(figsize=(10, 6))  # Definimos el tamaño de la figura
    plt.plot(arr, 'ro', label='Datos originales')  # Graficamos los datos originales
    plt.legend()
    plt.title('Datos originales antes del ordenamiento')
    plt.xlabel('Índice')
    plt.ylabel('Valor')
    plt.show()
    
    sorted_arr = tree_sort(arr)  # Ordenamos el arreglo usando el algoritmo de ordenamiento de árbol
    
    plt.figure(figsize=(10, 6))  # Definimos el tamaño de la figura
    plt.plot(sorted_arr, 'bo', label='Datos ordenados')  # Graficamos los datos ordenados
    plt.legend()
    plt.title('Datos después del ordenamiento (Tree Sort)')
    plt.xlabel('Índice')
    plt.ylabel('Valor')
    plt.show()

# Datos de ejemplo para ordenar
arr = [5, 3, 8, 4, 2, 7, 1, 10]

# Graficamos el proceso de ordenamiento
plot_sorting(arr)
