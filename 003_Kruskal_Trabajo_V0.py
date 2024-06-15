#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: Árbol de Máximo y Mínimo coste Kruskal - Trabajo

import matplotlib.pyplot as plt
import networkx as nx
import random

# Implementación del algoritmo de Kruskal
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
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

# Función para generar un grafo aleatorio de componentes y distancias
def generate_random_graph(num_components):
    components = [
        "Motor", "Sensor", "Actuador", "Controlador", "Cámara",
        "Válvula", "Bomba", "Placa Base", "Conector", "Interruptor"
    ][:num_components]
    edges = []
    for i in range(num_components):
        for j in range(i + 1, num_components):
            cost = random.randint(10, 100)  # Costo aleatorio entre 10 y 100 unidades monetarias
            edges.append((i, j, cost))
    return components, edges

# Función para aplicar Kruskal y visualizar la red de conexiones de costo mínimo
def visualize_mechatronic_network(num_components):
    components, edges = generate_random_graph(num_components)
    uf = UnionFind(num_components)
    mst = []
    total_cost = 0

    edges.sort(key=lambda x: x[2])  # Ordenar aristas por costo

    for u, v, cost in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, cost))
            total_cost += cost
            if len(mst) == num_components - 1:
                break

    G = nx.Graph()
    G.add_nodes_from(range(num_components))
    G.add_weighted_edges_from(mst)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, labels={i: components[i] for i in range(num_components)},
            node_color='lightblue', font_weight='bold', node_size=1000)

    edge_labels = {(u, v): f"${c}" for u, v, c in mst}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

    plt.title("Red de Conexiones de Componentes de Costo Mínimo en Ingeniería Mecatrónica")
    plt.text(0.5, 0.12, f"El grafo muestra componentes como nodos y conexiones seleccionadas con el mínimo "
                         f"costo total de ${total_cost} para el sistema mecatrónico.",
             horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes, fontsize=10)
    plt.show()

# Ejemplo de uso
if __name__ == "__main__":
    num_components = 5  # Número de componentes para el ejemplo
    visualize_mechatronic_network(num_components)
