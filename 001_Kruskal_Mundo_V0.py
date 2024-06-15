#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: Árbol de Máximo y Mínimo coste Kruskal - Mundo

import matplotlib.pyplot as plt
import networkx as nx

# Implementación de la estructura Union-Find para el algoritmo de Kruskal
class UnionFind:
    def __init__(self, n):
        """
        Inicializa la estructura Union-Find con n nodos.
        Cada nodo comienza siendo su propio padre (representante del conjunto).
        """
        self.parent = list(range(n))
        self.rank = [0] * n  # Rango para optimizar la unión por rango

    def find(self, u):
        """
        Encuentra el representante (raíz) del conjunto al que pertenece u.
        Realiza compresión de camino para mejorar la eficiencia en futuras búsquedas.
        """
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Compresión de camino
        return self.parent[u]

    def union(self, u, v):
        """
        Une los conjuntos que contienen a u y v.
        Utiliza unión por rango para mantener la estructura eficiente.
        """
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

# Función principal para el algoritmo de Kruskal
def kruskal(edges, num_vertices):
    """
    Implementa el algoritmo de Kruskal para encontrar el MST de un grafo dado.
    edges: lista de aristas (u, v, peso).
    num_vertices: número total de vértices en el grafo.
    Retorna las aristas del MST y su costo total.
    """
    # Ordenar las aristas por peso (tercer elemento de la tupla)
    edges.sort(key=lambda x: x[2])
    
    uf = UnionFind(num_vertices)  # Inicializar la estructura Union-Find
    mst = []  # Aristas del MST
    total_cost = 0  # Costo total del MST

    # Iterar sobre todas las aristas ordenadas
    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):  # Verificar si u y v están en diferentes conjuntos
            uf.union(u, v)  # Unir los conjuntos de u y v
            mst.append((u, v, weight))  # Agregar la arista al MST
            total_cost += weight  # Sumar al costo total del MST
            if len(mst) == num_vertices - 1:
                break  # Si ya se han agregado suficientes aristas (V-1), terminar

    return mst, total_cost

# Función para visualizar el grafo resultante
def visualize_graph(num_vertices, mst_edges, total_cost):
    """
    Visualiza el grafo resultante del MST utilizando Matplotlib y NetworkX.
    num_vertices: número total de vértices en el grafo.
    mst_edges: lista de aristas que forman el MST.
    total_cost: costo total del MST.
    """
    G = nx.Graph()  # Crear un grafo vacío
    G.add_nodes_from(range(num_vertices))  # Agregar nodos al grafo

    # Agregar aristas al grafo
    edge_list = [(u, v) for u, v, weight in mst_edges]
    G.add_edges_from(edge_list)
    
    # Dibujar el grafo utilizando NetworkX y Matplotlib
    pos = nx.spring_layout(G)  # Posiciones de los nodos para visualización
    labels = {i: f"Ciudad {i}" for i in range(num_vertices)}  # Etiquetas de los nodos

    # Dibujar nodos con etiquetas y colores específicos
    nx.draw(G, pos, with_labels=True, labels=labels, node_color='lightblue', font_weight='bold', node_size=1000)

    # Dibujar aristas con etiquetas de peso
    nx.draw_networkx_edges(G, pos, edgelist=edge_list, edge_color='blue', width=2)
    edge_labels = {(u, v): f"{w}" for u, v, w in mst_edges}  # Etiquetas de las aristas
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', label_pos=0.3)

    # Anotaciones para explicar el gráfico
    plt.title("Red de Carreteras de Costo Mínimo (Kruskal)")
    plt.text(0.5, 0.8, f"El grafo muestra las ciudades como nodos y las carreteras seleccionadas como aristas.\n"
                         f"El MST conecta todas las ciudades con el mínimo costo total de {total_cost}.",
             horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes, fontsize=10)
    plt.show()

# Ejemplo de uso
if __name__ == "__main__":
    # Ejemplo de grafo con 5 ciudades y las conexiones entre ellas (u, v, peso)
    edges = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]
    num_vertices = 4

    # Aplicar el algoritmo de Kruskal para encontrar el MST y el costo total
    mst, total_cost = kruskal(edges, num_vertices)
    print("Árbol de Expansión Mínima (MST):", mst)
    print("Costo Total:", total_cost)

    # Visualizar el grafo resultante con Matplotlib y NetworkX
    visualize_graph(num_vertices, mst, total_cost)


