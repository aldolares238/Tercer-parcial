#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: Árbol Parcial mínimo de Prim. - Mundo


import heapq
import matplotlib.pyplot as plt
import networkx as nx

# Diccionario que representa el grafo: cada nodo (fuente o parcela) y las conexiones (aristas) con sus costos (pesos)
graph = {
    'A': [('B', 1), ('C', 3), ('D', 4), ('E', 2)],
    'B': [('A', 1), ('C', 2), ('E', 3)],
    'C': [('A', 3), ('B', 2), ('D', 4), ('E', 5)],
    'D': [('A', 4), ('C', 4), ('E', 6)],
    'E': [('A', 2), ('B', 3), ('C', 5), ('D', 6)]
}


def prim(graph):
    start_node = list(graph.keys())[0]
    visited = set([start_node])
    edges = [(weight, start_node, to) for to, weight in graph[start_node]]
    heapq.heapify(edges)
    mst = []
    
    while edges:
        weight, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, weight))
            
            for to_next, weight_next in graph[to]:
                if to_next not in visited:
                    heapq.heappush(edges, (weight_next, to, to_next))
    
    return mst

mst = prim(graph)
print("Árbol de Expansión Mínimo:", mst)


# Posiciones fijas de los nodos para visualización
pos = {'A': (0, 0), 'B': (1, 2), 'C': (2, 1), 'D': (3, 0), 'E': (1, -2)}

# Crear el grafo usando NetworkX
G = nx.Graph()
for frm in graph:
    for to, weight in graph[frm]:
        G.add_edge(frm, to, weight=weight)

# Dibujar el grafo original con todas las aristas y sus pesos
plt.figure(figsize=(10, 6))
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Dibujar el MST resultante, resaltando las aristas en rojo
mst_edges = [(frm, to) for frm, to, weight in mst]
nx.draw_networkx_edges(G, pos, edgelist=mst_edges, width=2, edge_color='r')

# Añadir título y leyenda explicativa
plt.title("Sistema de Riego: Árbol de Expansión Mínimo (MST)")
plt.text(1.55, 2, "Nodos: Fuentes de agua y parcelas agrícolas\nAristas: Costos de las tuberías\nRojo: Conexiones seleccionadas para el MST", fontsize=12, bbox=dict(facecolor='white', alpha=0.6))

# Mostrar el gráfico
plt.show()
