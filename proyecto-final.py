import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix

def load_tsp_instance(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    # Extraer las coordenadas
    coordinates = []    
    for line in lines[6:]: 
        # Ignorar las primeras 6 líneas
        parts = line.split()
        if len(parts) >= 3:
            x, y = float(parts[1]), float(parts[2])
            coordinates.append((x, y))
    return np.array(coordinates)

def calculate_distance_matrix(coordinates):
    # Calcular la matriz de distancias entre las coordenadas
    return distance_matrix(coordinates, coordinates)

def nearest_neighbor(graph, start):
    visited = [start]
    current = start
    while len(visited) < len(graph):
        # Encontrar la ciudad más cercana que no ha sido visitada
        next_city = min((node for node in range(len(graph)) if node not in visited), key=lambda x: graph[current][x])
        visited.append(next_city) 
        current = next_city 
    return visited

def minimum_spanning_tree(graph):
    # Crear un árbol de expansión mínima (MST)
    G = nx.Graph(graph)
    mst = nx.minimum_spanning_tree(G)
    return mst

def odd_degree_vertices(mst):
    # Encontrar los vértices de grado impar en el MST
    return [v for v in mst.nodes if mst.degree[v] % 2 == 1]

def eulerian_circuit(graph, start):
    # Encontrar un circuito euleriano en el grafo
    G = nx.Graph(graph)
    tour = list(nx.eulerian_circuit(G, source=start))
    return [u for u, v in tour] + [tour[0][1]]  # Regresar al inicio

def christofides_algorithm(graph):
    # Paso 1: Crear un árbol de expansión mínima (MST)
    mst = minimum_spanning_tree(graph)
    # Paso 2: Encontrar los vértices de grado impar
    odd_vertices = odd_degree_vertices(mst)
    
    # Paso 3: Encontrar el emparejamiento perfecto de peso mínimo para los vértices de grado impar
    matching_graph = nx.complete_graph(odd_vertices)
    for i in range(len(odd_vertices)):
        for j in range(i + 1, len(odd_vertices)):
            # Asignar pesos a las aristas del grafo de emparejamiento
            matching_graph[odd_vertices[i]][odd_vertices[j]]['weight'] = graph[odd_vertices[i]][odd_vertices[j]]
    
    # Encontrar el emparejamiento de peso mínimo
    matching = nx.algorithms.matching.min_weight_matching(matching_graph, maxcardinality=True)
    
    # Paso 4: Combinar el MST y el emparejamiento
    combined_graph = nx.Graph()
    combined_graph.add_edges_from(mst.edges(data=True))
    combined_graph.add_edges_from(matching)
    
    # Paso 5: Encontrar el circuito euleriano
    start = mst.nodes[0]
    eulerian_tour = eulerian_circuit(combined_graph, start)
    
    # Paso 6: Convertir el circuito euleriano en un circuito hamiltoniano
    hamiltonian_circuit = []
    visited = set()
    for node in eulerian_tour:
        if node not in visited: 
            hamiltonian_circuit.append(node)
            visited.add(node)
    
    return hamiltonian_circuit

# Ejecución principal
if __name__ == "__main__":
    # Cargar la instancia pla85900
    coordinates = load_tsp_instance('pla33810.tsp')
    distance_matrix = calculate_distance_matrix(coordinates)
    # Ejecutar el algoritmo de Christofides
    tour = christofides_algorithm(distance_matrix)
    print("Tour encontrado:", tour)