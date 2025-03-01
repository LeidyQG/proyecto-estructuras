import time

import numpy as np
from scipy.spatial import distance_matrix

from ..app_globals import get_file_path, set_file_results, set_file_processed

def leer_instancia_tsp(archivo):
    with open(archivo, 'r') as f:
        lineas = f.readlines()
    
    # Extraer las coordenadas de las ciudades
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
            if len(partes) == 3:  # Asumiendo formato: id x y
                coordenadas.append((float(partes[1]), float(partes[2])))
    
    return np.array(coordenadas)

def delta_tsp_vecino_mas_cercano(coordenadas):
    n = len(coordenadas)
    distancias = distance_matrix(coordenadas, coordenadas)
    visitado = [False] * n
    ruta = [0]  # Empezar en la primera ciudad
    visitado[0] = True
    
    for _ in range(1, n):
        ultima_ciudad = ruta[-1]
        distancias_minimas = np.where(visitado, np.inf, distancias[ultima_ciudad])
        ciudad_mas_cercana = np.argmin(distancias_minimas)
        ruta.append(ciudad_mas_cercana)
        visitado[ciudad_mas_cercana] = True
    
    # Calcular el delta (diferencia entre la arista más larga y la más corta)
    aristas = [distancias[ruta[i], ruta[i+1]] for i in range(n-1)]
    aristas.append(distancias[ruta[-1], ruta[0]])  # Cerrar el ciclo
    delta = max(aristas) - min(aristas)
    
    return ruta, delta

def neighbor_delta_algorithm (parent):
    archivo_tsp = str(get_file_path())

    coordenadas = leer_instancia_tsp(archivo_tsp)
    inicio = time.time()
    ruta, delta = delta_tsp_vecino_mas_cercano(coordenadas)
    fin = time.time()
 
    set_file_processed(True, parent)
    set_file_results({
        "distance": delta,
        "nodes": len(coordenadas),
        "route": ruta,
        "time": fin - inicio
    }, parent)

    # print(f"Ruta encontrada: {ruta}")
    # print(f"Delta (diferencia entre arista más larga y más corta): {delta}")
    # print(f"Tiempo de ejecución: {fin - inicio:.4f} segundos")

if __name__ == "__main__":
    archivo_tsp = "ulysses22.tsp"
    main(archivo_tsp)
