import numpy as np
import ctypes
import os
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.spatial import distance_matrix

# Cargar la biblioteca compartida de C++
lib = ctypes.CDLL('./distance_calculator.so')
lib.calculate_distance_matrix.argtypes = (
    ctypes.POINTER(ctypes.c_double),  # cities
    ctypes.c_int,                     # num_cities
    ctypes.POINTER(ctypes.c_double)   # distance_matrix
)

def read_tsp_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    node_coord_section = False
    cities = []
    
    for line in lines:
        if "NODE_COORD_SECTION" in line:
            node_coord_section = True
            continue
        if "EOF" in line:
            break
        if node_coord_section:
            parts = line.strip().split()
            cities.append((float(parts[1]), float(parts[2])))
    
    return np.array(cities, dtype=np.float64)

def calculate_distance_matrix_parallel(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities), dtype=np.float64)
    
    # Convertir ciudades a un array de C
    cities_c = cities.flatten().ctypes.data_as(ctypes.POINTER(ctypes.c_double))
    distance_matrix_c = distance_matrix.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
    
    # Llamar a la función de C++ para calcular la matriz de distancias
    lib.calculate_distance_matrix(cities_c, num_cities, distance_matrix_c)
    
    return distance_matrix

def mst_approximation_tsp(distance_matrix):
    mst = minimum_spanning_tree(distance_matrix)
    mst = mst.toarray()
    
    # Recorrido en preorden
    def preorder_traversal(node, visited, tour):
        visited[node] = True
        tour.append(node)
        for i in range(len(mst)):
            if mst[node][i] > 0 and not visited[i]:
                preorder_traversal(i, visited, tour)
    
    visited = [False] * len(mst)
    tour = []
    preorder_traversal(0, visited, tour)
    
    # Regresar al punto de inicio
    tour.append(0)
    
    return tour

def calculate_tour_distance(tour, distance_matrix):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distance_matrix[tour[i]][tour[i+1]]
    return total_distance

def save_distance_matrix_to_disk(distance_matrix, file_path):
    with open(file_path, 'wb') as f:
        np.save(f, distance_matrix)

def load_distance_matrix_from_disk(file_path):
    with open(file_path, 'rb') as f:
        return np.load(f)

def main(file_path):
    cities = read_tsp_file(file_path)
    print(f"Number of cities: {len(cities)}")
    
    # Calcular la matriz de distancias en paralelo
    distance_matrix_path = "distance_matrix.npy"
    if not os.path.exists(distance_matrix_path):
        print("Calculating distance matrix...")
        distance_matrix = calculate_distance_matrix_parallel(cities)
        save_distance_matrix_to_disk(distance_matrix, distance_matrix_path)
    else:
        print("Loading distance matrix from disk...")
        distance_matrix = load_distance_matrix_from_disk(distance_matrix_path)
    
    # Aproximación del TSP
    print("Approximating TSP solution...")
    tour = mst_approximation_tsp(distance_matrix)
    total_distance = calculate_tour_distance(tour, distance_matrix)
    
    print(f"Tour: {tour}")
    print(f"Total Distance: {total_distance}")

if __name__ == "__main__":
    file_path = "ruta_al_archivo.tsp"  # Cambia esto por la ruta de tu archivo .tsp
    main(file_path)
