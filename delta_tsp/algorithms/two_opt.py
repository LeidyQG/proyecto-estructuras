import time

import numpy as np
from scipy.spatial import distance_matrix

from tkinter import Misc

from ..app_globals import set_file_processed, set_file_results, get_file_path

def read_tsp_file (archivo):
    with open(archivo, 'r') as f:
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

def get_nearest_neighbor (coordenadas, distancias):
    n = len(coordenadas)
    visitado = np.zeros(n, dtype=bool)
    ruta = [0]  # Empezar en la primera ciudad
    visitado[0] = True
    
    for _ in range(1, n):
        ultima_ciudad = ruta[-1]
        distancias_minimas = np.where(visitado, np.inf, distancias[ultima_ciudad])
        ciudad_mas_cercana = np.argmin(distancias_minimas)
        ruta.append(ciudad_mas_cercana)
        visitado[ciudad_mas_cercana] = True
    
    return ruta

def calc_total_distance (ruta, distancias):
    return sum(distancias[ruta[i], ruta[i+1]] for i in range(len(ruta)-1)) + distancias[ruta[-1], ruta[0]]

def two_opt (ruta, distancias, max_iteraciones=100):
    mejor_ruta = ruta
    mejor_distancia = calc_total_distance(mejor_ruta, distancias)
    
    for _ in range(max_iteraciones):
        mejora = False
        for i in range(1, len(ruta) - 2):
            for j in range(i + 1, len(ruta) - 1):
                if j - i == 1:
                    continue
                
                # Calcular el cambio en la distancia sin copiar la ruta
                delta = (distancias[mejor_ruta[i-1], mejor_ruta[j]] +
                         distancias[mejor_ruta[i], mejor_ruta[j+1]]) - \
                        (distancias[mejor_ruta[i-1], mejor_ruta[i]] +
                         distancias[mejor_ruta[j], mejor_ruta[j+1]])
                
                if delta < 0:
                    mejor_ruta[i:j+1] = mejor_ruta[j:i-1:-1]
                    mejor_distancia += delta
                    mejora = True
        
        if not mejora:
            break
    
    return mejor_ruta

def two_opt_algorithm (parent: Misc) -> None:
    file_path = str(get_file_path())

    start_time = time.time()
    coordinates_array = read_tsp_file(file_path)
    distances_array = distance_matrix(coordinates_array, coordinates_array)

    starting_route = get_nearest_neighbor(coordinates_array, distances_array)
    starting_distance = calc_total_distance(starting_route, distances_array)

    optimal_route = two_opt(starting_route, distances_array)
    optimal_distance = calc_total_distance(optimal_route, distances_array)

    set_file_processed(True, parent)
    set_file_results({
        "distance": optimal_distance,
        "time": time.time() - start_time,
        "route": optimal_route,
        "nodes": len(coordinates_array)
    }, parent)

