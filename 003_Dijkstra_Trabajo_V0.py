#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: Algoritmo de Dijkstra - Trabajo

import heapq
import matplotlib.pyplot as plt
import networkx as nx

# Definimos el grafo con los tiempos de viaje en minutos
grafo = {
    'Cuadrilla1': {'Nodo1': 15},
    'Nodo1': {'Emergencia': 30},
    'Cuadrilla2': {'Nodo2': 10},
    'Nodo2': {'Emergencia': 45},
    'Cuadrilla3': {'Nodo3': 20},
    'Nodo3': {'Emergencia': 20},
    'Emergencia': {}
}

def dijkstra(grafo, inicio, fin):
    distancias = {nodo: float('infinity') for nodo in grafo}
    distancias[inicio] = 0
    padres = {nodo: None for nodo in grafo}
    
    cola_prioridad = [(0, inicio)]
    
    while cola_prioridad:
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
    
    return distancias[fin], camino

def mostrar_grafo(grafo, ruta, peso_total):
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
    plt.title(f"Ruta más corta: {ruta_texto}\nPeso total: {peso_total} minutos", fontsize=15)
    
    # Añadir el peso total en el gráfico
    plt.text(0.5, 0.1, f'Peso total de la ruta: {peso_total} minutos', horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes, fontsize=12, bbox=dict(facecolor='white', alpha=0.6))
    plt.text(0.5, 0.15, f'La mejor cuadrilla para esta situacion es {mejor_cuadrilla[1]}', horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes, fontsize=12, bbox=dict(facecolor='white', alpha=0.6))
    plt.show()

# Definimos los nodos de inicio y fin
inicio1 = 'Cuadrilla1'
inicio2 = 'Cuadrilla2'
inicio3 = 'Cuadrilla3'
fin = 'Emergencia'

# Ejecución del algoritmo desde cada cuadrilla hasta el punto de emergencia
peso_total1, ruta1 = dijkstra(grafo, inicio1, fin)
peso_total2, ruta2 = dijkstra(grafo, inicio2, fin)
peso_total3, ruta3 = dijkstra(grafo, inicio3, fin)

# Determinar la cuadrilla más rápida
mejor_cuadrilla = min([(peso_total1, 'Cuadrilla1', ruta1), (peso_total2, 'Cuadrilla2', ruta2), (peso_total3, 'Cuadrilla3', ruta3)])
print(f"La mejor cuadrilla es {mejor_cuadrilla[1]} con un tiempo de {mejor_cuadrilla[0]} minutos")

# Visualización del grafo y la ruta más corta para la mejor cuadrilla
mostrar_grafo(grafo, mejor_cuadrilla[2], mejor_cuadrilla[0])

