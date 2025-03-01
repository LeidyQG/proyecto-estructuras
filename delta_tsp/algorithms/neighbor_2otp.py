import time

import numpy as np
from scipy.spatial import distance_matrix

from ..app_globals import get_file_path, set_file_processed, set_file_results

def leer_instancia_tsp(archivo):
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

def vecino_mas_cercano(coordenadas, distancias):
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

def calcular_distancia_total(ruta, distancias):
    return sum(distancias[ruta[i], ruta[i+1]] for i in range(len(ruta)-1)) + distancias[ruta[-1], ruta[0]]

def two_opt(ruta, distancias, max_iteraciones=100):
    mejor_ruta = ruta
    mejor_distancia = calcular_distancia_total(mejor_ruta, distancias)
    
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

def neighbor_opt_algorithm (parent):
    coordenadas = leer_instancia_tsp(str(get_file_path()))
    distancias = distance_matrix(coordenadas, coordenadas)
    
    # Paso 1: Generar solución inicial con Vecino más cercano
    inicio = time.time()
    ruta_inicial = vecino_mas_cercano(coordenadas, distancias)
    distancia_inicial = calcular_distancia_total(ruta_inicial, distancias)
    # print(f"Distancia inicial (Vecino más cercano): {distancia_inicial}")
    # print(f"Tiempo Vecino más cercano: {time.time() - inicio:.4f} segundos")
    
    # Paso 2: Mejorar la solución con 2-opt
    # inicio = time.time()
    ruta_optimizada = two_opt(ruta_inicial, distancias)
    distancia_optimizada = calcular_distancia_total(ruta_optimizada, distancias)
    # print(f"Distancia optimizada (2-opt): {distancia_optimizada}")
    # print(f"Tiempo 2-opt: {time.time() - inicio:.4f} segundos")

    set_file_processed(True, parent)
    set_file_results({
        "distance": distancia_optimizada,
        "route": ruta_optimizada,
        "nodes": len(coordenadas),
        "time": time.time() - inicio
    }, parent)

def main(archivo_tsp):
    coordenadas = leer_instancia_tsp(archivo_tsp)
    distancias = distance_matrix(coordenadas, coordenadas)
    
    # Paso 1: Generar solución inicial con Vecino más cercano
    inicio = time.time()
    ruta_inicial = vecino_mas_cercano(coordenadas, distancias)
    distancia_inicial = calcular_distancia_total(ruta_inicial, distancias)
    print(f"Distancia inicial (Vecino más cercano): {distancia_inicial}")
    print(f"Tiempo Vecino más cercano: {time.time() - inicio:.4f} segundos")
    
    # Paso 2: Mejorar la solución con 2-opt
    inicio = time.time()
    ruta_optimizada = two_opt(ruta_inicial, distancias)
    distancia_optimizada = calcular_distancia_total(ruta_optimizada, distancias)
    print(f"Distancia optimizada (2-opt): {distancia_optimizada}")
    print(f"Tiempo 2-opt: {time.time() - inicio:.4f} segundos")
    
    

if __name__ == "__main__":
    archivo_tsp = "./ulysses22.tsp"  # Cambia esto por el nombre de tu archivo .tsp
    main(archivo_tsp)
