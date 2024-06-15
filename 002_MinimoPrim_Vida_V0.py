#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: Árbol Parcial mínimo de Prim. - Vida


import heapq
import matplotlib.pyplot as plt
import networkx as nx

# Definir el grafo con nodos y aristas
graph = {
    'Aula': [('Biblioteca', 3), ('Cafetería', 5)],
    'Biblioteca': [('Aula', 3), ('Cafetería', 1), ('Gimnasio', 7)],
    'Cafetería': [('Aula', 5), ('Biblioteca', 1), ('Gimnasio', 2)],
    'Gimnasio': [('Biblioteca', 7), ('Cafetería', 2)]
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

# Calcular el Árbol de Expansión Mínimo (MST)
mst = prim(graph)
print("Árbol de Expansión Mínimo:", mst)

# Posiciones fijas de los nodos para visualización
pos = {'Aula': (1, 3), 'Biblioteca': (4, 3), 'Cafetería': (4, 0), 'Gimnasio': (6, 1)}

# Crear el grafo usando NetworkX
G = nx.Graph()
for frm in graph:
    for to, weight in graph[frm]:
        G.add_edge(frm, to, weight=weight)

# Crear figuras y ejes para subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Dibujar el grafo original con todas las aristas y sus pesos
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=12, font_weight='bold', ax=ax1)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=12, font_weight='bold', ax=ax1)

# Dibujar el MST resultante, resaltando las aristas en rojo
mst_edges = [(frm, to) for frm, to, weight in mst]
nx.draw_networkx_edges(G, pos, edgelist=mst_edges, width=2, edge_color='r', ax=ax1)

# Mostrar la explicación
ax2.text(0, 1, 
         "Este gráfico muestra la mejor manera de recorrer los puntos de interés del campus universitario \n"
         "(Aula, Biblioteca, Cafetería y Gimnasio) minimizando la distancia total.\n\n"
         "Nodos:\n"
         " - Aula principal\n"
         " - Biblioteca\n"
         " - Cafetería\n"
         " - Gimnasio\n\n"
         "Aristas y Pesos: Las conexiones entre los puntos y sus distancias respectivas.\n\n"
         "Aristas en Rojo: Caminos seleccionados para formar el Árbol de Expansión Mínimo (MST), \n"
         "indicando la ruta más eficiente para conectar todos los puntos minimizando la distancia total.\n\n"
         "Interpretación:\n"
         "1. Comienza desde Aula y sigue los caminos en rojo para conectar todos los puntos.\n"
         "2. Este recorrido garantiza que la distancia total es la mínima posible.",
         fontsize=12, bbox=dict(facecolor='white', alpha=0.8), ha='left', va='top', wrap=True)
ax2.axis('off')  # Deshabilitar los ejes

# Mostrar los subplots
plt.show()

