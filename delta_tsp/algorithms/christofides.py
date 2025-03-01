
import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix

from tkinter import Misc

from ..app_globals import get_file_path, set_file_processed, set_file_results

# from ..app_globals import get_file_path, set_file_processed

def load_tsp_instance(file_path: str) -> np.array:
    with open(file_path, 'r') as f:
        lineas = f.readlines()
    
    coordenadas = []
    leer_coordenadas = False
    for linea in lineas:
        if linea.startswith("NODE_COORD_SECTION"):
            leer_coordenadas = True
            continue
        if linea.startswith("EOF"):
            break
        if leer_coordenadas:
            partes = linea.strip().split()
            if len(partes) == 3:
                coordenadas.append((float(partes[1]), float(partes[2])))

    return np.array(coordenadas)

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

def christofides (graph):
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
    matching = nx.algorithms.matching.min_weight_matching(matching_graph)
    
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

def christofides_algorithm (parent: Misc) -> None:
    file_path: str = str(get_file_path())

    coordinates_array: np.array = load_tsp_instance(file_path)
    distance_matrix = calculate_distance_matrix(coordinates_array)
    tour = christofides(distance_matrix)

    set_file_processed(True, parent=parent)


# Ejecución principal
if __name__ == "__main__":
    # Cargar la instancia pla85900
    coordinates = load_tsp_instance('../../ulysses22-2.tsp')
    distance_matrix = calculate_distance_matrix(coordinates)
    # Ejecutar el algoritmo de Christofides
    tour = christofides(distance_matrix)
    print("Tour encontrado:", tour)
