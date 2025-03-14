import numpy as np
import random

def read_tsp_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    coords = []
    for line in lines:
        if line.startswith('EOF'):
            break
        if line[0].isdigit():
            parts = line.split()
            coords.append((float(parts[1]), float(parts[2])))
    
    return np.array(coords)

def calculate_distance(point1, point2):
    return np.linalg.norm(point1 - point2)

def total_distance(tour, coords):
    return sum(calculate_distance(coords[tour[i]], coords[tour[i - 1]]) for i in range(len(tour)))

def two_opt(tour, coords):
    best = tour
    best_distance = total_distance(best, coords)
    
    for i in range(len(tour)):
        for j in range(i + 1, len(tour)):
            if j - i == 1:  # Skip adjacent nodes
                continue
            
            new_tour = best[:]
            new_tour[i:j] = reversed(best[i:j])
            new_distance = total_distance(new_tour, coords)
            
            if new_distance < best_distance:
                best = new_tour
                best_distance = new_distance
    
    return best

def generate_initial_tour(num_cities):
    tour = list(range(num_cities))
    random.shuffle(tour)
    return tour

def delta_tsp(filename):
    coords = read_tsp_file(filename)
    num_cities = len(coords)
    
    # Genera un tour inicial aleatorio
    initial_tour = generate_initial_tour(num_cities)
    
    # Aplica el algotimo 2-opt para mejorar el tour aleayotio inical
    optimized_tour = two_opt(initial_tour, coords)
    
    return optimized_tour, total_distance(optimized_tour, coords)

if __name__ == "__main__":
    filename = "pla33810.tsp"  
    tour, distance = delta_tsp(filename)
    
    print("Tour optimizado:", tour)
    print("Distancia total:", distance)
