#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: Algoritmo de Dijkstra - En el mundo

import heapq
import matplotlib.pyplot as plt
import networkx as nx

# Definimos el grafo como un diccionario de diccionarios
grafo = {
    'A': {'B': 2, 'D': 1, 'E': 3},
    'B': {'A': 2, 'C': 4, 'E': 1},
    'C': {'B': 4, 'F': 2},
    'D': {'A': 1, 'E': 7},
    'E': {'A': 3, 'B': 1, 'D': 7, 'F': 5},
    'F': {'C': 2, 'E': 5}
}

def dijkstra(grafo, inicio, fin): #Definición de la funcion para la busqueda
    distancias = {nodo: float('infinity') for nodo in grafo}
    distancias[inicio] = 0
    padres = {nodo: None for nodo in grafo}
    
    cola_prioridad = [(0, inicio)]
    
    while cola_prioridad: #Añadimos el ciclo para la prioridad del camino
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)
        
        if nodo_actual == fin:
            break
        
        if distancia_actual > distancias[nodo_actual]:
            continue
        
        for vecino, peso in grafo[nodo_actual].items(): 
            distancia = distancia_actual + peso
            
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                padres[vecino] = nodo_actual
                heapq.heappush(cola_prioridad, (distancia, vecino))
    
    camino = []
    nodo = fin
    while nodo is not None:
        camino.append(nodo)
        nodo = padres[nodo]
    camino.reverse()
    
    return distancias, camino

def mostrar_grafo(grafo, ruta, peso_total): #Funcion para mostrar el grafo al usuario
    G = nx.Graph()
    
    for nodo in grafo:
        for vecino, peso in grafo[nodo].items():
            G.add_edge(nodo, vecino, weight=peso)
    
    pos = nx.spring_layout(G)
    
    plt.figure(figsize=(10, 8))
    
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=12, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)}, font_size=12)
    
    if ruta:
        path_edges = list(zip(ruta, ruta[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)
        nx.draw_networkx_nodes(G, pos, nodelist=ruta, node_color='r', node_size=700)
    
    ruta_texto = " -> ".join(ruta)
    plt.title(f"Ruta más corta: {ruta_texto}\nPeso total: {peso_total}", fontsize=15)
    
    # Añadir el peso total en el gráfico
    plt.text(0.5, 0.1, f'Peso total de la ruta: {peso_total}', horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes, fontsize=12, bbox=dict(facecolor='white', alpha=0.6))
    
    plt.show()

# Definimos los nodos de inicio y fin
inicio = 'A'
fin = 'F'

# Ejecución del algoritmo desde el nodo 'inicio' al nodo 'fin'
distancias, ruta = dijkstra(grafo, inicio, fin)
peso_total = distancias[fin]

print(f"Distancias desde {inicio}: {distancias}")
print(f"Ruta más corta desde {inicio} hasta {fin}: {ruta}")
print(f"Peso total de la ruta: {peso_total}")

# Visualización del grafo y la ruta más corta
mostrar_grafo(grafo, ruta, peso_total)

