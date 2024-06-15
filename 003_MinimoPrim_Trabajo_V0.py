#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: Árbol Parcial mínimo de Prim. - Trabajo

import heapq
import matplotlib.pyplot as plt
import networkx as nx

# Definir el grafo con nodos y aristas (ubicaciones y distancias)
graph = {
    'Materia Prima': [('Procesado', 7), ('Ensamblaje', 8)],
    'Procesado': [('Materia Prima', 7), ('Ensamblaje', 3), ('Producción', 6)],
    'Ensamblaje': [('Materia Prima', 8), ('Procesado', 3), ('Producción', 4)],
    'Producción': [('Procesado', 6), ('Ensamblaje', 4), ('Almacén', 2)],
    'Almacén': [('Producción', 2)]
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
pos = {'Materia Prima': (0, 0), 'Procesado': (1, 2), 'Ensamblaje': (2, 1), 'Producción': (3, 0), 'Almacén': (4, -1)}

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
         "Este gráfico muestra la disposición óptima de las estaciones de trabajo en una nave industrial minimizando la longitud total de las conexiones necesarias.\n\n"
         "Nodos:\n"
         " - Materia Prima\n"
         " - Procesado\n"
         " - Ensamblaje\n"
         " - Producción\n"
         " - Almacén\n\n"
         "Aristas y Pesos: Las conexiones entre las estaciones y sus distancias respectivas.\n\n"
         "Aristas en Rojo: Conexiones seleccionadas para formar el Árbol de Expansión Mínimo (MST), \n"
         "indicando la ruta más eficiente para conectar todas las estaciones minimizando la longitud total.\n\n"
         "Interpretación:\n"
         "1. Comienza desde una estación y sigue las conexiones en rojo para conectar todas las estaciones.\n"
         "2. Este diseño garantiza que la longitud total de las conexiones es la mínima posible.",
         fontsize=12, bbox=dict(facecolor='white', alpha=0.8), ha='left', va='top', wrap=True)
ax2.axis('off')  # Deshabilitar los ejes

# Mostrar los subplots
plt.show()
