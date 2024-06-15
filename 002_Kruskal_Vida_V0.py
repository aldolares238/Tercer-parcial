#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: Árbol de Máximo y Mínimo coste Kruskal - Vida

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

# Función para generar un grafo aleatorio de ciudades y distancias
def generate_random_graph(num_cities):
    # Nombres de Pueblos Mágicos de Jalisco
    cities = [
        "Tapalpa", "Mazamitla", "Tlaquepaque", "Tequila", "Ajijic",
        "Chapala", "San Sebastián del Oeste", "Lagos de Moreno", "San Juan de los Lagos", "Mascota"
    ][:num_cities]
    edges = []
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            distance = random.randint(5, 30)  # Distancia aleatoria entre 5 y 30 kilómetros
            edges.append((i, j, distance))
    return cities, edges

# Función para aplicar Kruskal y visualizar el MST
def visualize_travel_plan(num_cities):
    cities, edges = generate_random_graph(num_cities)
    uf = UnionFind(num_cities)
    mst = []
    total_distance = 0

    edges.sort(key=lambda x: x[2])  # Ordenar aristas por distancia

    for u, v, distance in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, distance))
            total_distance += distance
            if len(mst) == num_cities - 1:
                break

    G = nx.Graph()
    G.add_nodes_from(range(num_cities))
    G.add_weighted_edges_from(mst)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, labels={i: cities[i] for i in range(num_cities)},
            node_color='lightblue', font_weight='bold', node_size=1000)

    edge_labels = {(u, v): f"{d} km" for u, v, d in mst}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

    plt.title("Itinerario de Viaje de Costo Mínimo entre Pueblos Mágicos de Jalisco")
    plt.text(0.5, 0.12, f"El grafo muestra Pueblos Mágicos de Jalisco como nodos y caminos seleccionados con el mínimo "
                         f"costo total de viaje de {total_distance} kilómetros.",
             horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes, fontsize=10)
    plt.show()

# Ejemplo de uso
if __name__ == "__main__":
    num_cities = 5  # Número de Pueblos Mágicos para el ejemplo
    visualize_travel_plan(num_cities)



