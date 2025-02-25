# README: CC - Delta TSP Solver- GUI
## Descripción General

El CC - Delta TSP Solver es una aplicación gráfica diseñada para resolver instancias del problema del Viajante de Comercio (TSP, por sus siglas en inglés). La aplicación está construida utilizando la biblioteca `tkinter` de Python, con extensiones de `tkinterdnd2` para soportar la funcionalidad de arrastrar y soltar archivos. La interfaz gráfica está organizada en varias secciones que permiten al usuario cargar archivos de instancias TSP, procesarlos utilizando diferentes algoritmos y visualizar los resultados.

## Estructura del Proyecto

El proyecto está organizado en varios módulos y archivos que gestionan diferentes aspectos de la interfaz gráfica y la lógica de la aplicación. 


## Instalación y Ejecución

# Proyecto de Análisis de Redes y Optimización

Este proyecto utiliza bibliotecas de Python para el análisis de redes, optimización y visualización.

## Requisitos

Antes de ejecutar el proyecto, asegúrate de instalar las siguientes dependencias:

```
networkx==3.4.2
numpy==2.2.3
scipy==1.15.2
tkinterdnd2==0.4.2
c++==11.0.0 o superior
pyhton==3.0.0 o superior
```

Puedes instalarlas con el siguiente comando:

```
pip install -r requirements.txt
```

## Uso de la Aplicación

1. **Cargar un Archivo TSP**:
   - En la pestaña "Load", puedes cargar un archivo TSP utilizando el botón "Find File" o arrastrando y soltando el archivo en la ventana.
   - Una vez cargado el archivo, la pestaña "Process" se habilitará automáticamente.

2. **Procesar el Archivo**:
   - En la pestaña "Process", puedes previsualizar el contenido del archivo cargado.
   - Selecciona uno de los algoritmos disponibles para procesar el archivo.

3. **Ver Resultados**:
   - Después de procesar el archivo, los resultados se mostrarán en la pestaña "Results".

# README: Implementaciones de Algoritmos para el Problema del Viajante de Comercio (DELTA-TSP)

Este repositorio contiene cinco implementaciones de algoritmos para resolver el Problema del Viajante de Comercio (TSP). Cada algoritmo tiene su propio enfoque y características, lo que permite comparar su rendimiento y resultados. 

---

## 1. **Algoritmo de Christofides**

### Descripción
El algoritmo de Christofides es una aproximación clásica para resolver el TSP. Combina un Árbol de Expansión Mínima (MST) con un emparejamiento perfecto de peso mínimo para construir un circuito euleriano, que luego se convierte en un circuito hamiltoniano.

#### Resultados:
- Imprime el recorrido (tour) encontrado por el algoritmo.

---

## 2. **Algoritmo 2-opt**

### Descripción
El algoritmo 2-opt es una técnica de optimización local que mejora una solución inicial (por ejemplo, un tour aleatorio) intercambiando pares de aristas para reducir la distancia total del recorrido.

#### Resultados:
- Imprime el recorrido optimizado y la distancia total.

---

## 3. **Algoritmo del Vecino Más Cercano con Delta**

### Descripción
Este algoritmo utiliza la heurística del vecino más cercano para construir un recorrido inicial y luego calcula el delta (diferencia entre la arista más larga y la más corta) como métrica de calidad.

#### Resultados:
- Imprime el recorrido encontrado, el delta y el tiempo de ejecución.

---

## 4. **Algoritmo Híbrido: Vecino Más Cercano + 2-opt**

### Descripción
Este algoritmo combina la heurística del vecino más cercano para generar una solución inicial y luego aplica el algoritmo 2-opt para optimizar el recorrido.

#### Resultados:
- Imprime la distancia inicial (vecino más cercano), la distancia optimizada (2-opt) y los tiempos de ejecución.

---

## 5. **Algoritmo de Cálculo de Matriz de Distancias en Paralelo (C++ y Python)**

### Descripción
Este algoritmo utiliza una implementación en C++ para calcular la matriz de distancias entre ciudades en paralelo, lo que mejora significativamente el rendimiento en comparación con una implementación secuencial. Luego, utiliza un enfoque basado en el Árbol de Expansión Mínima (MST) para aproximar una solución al TSP.

#### Resultados:
- Imprime el número de ciudades, la matriz de distancias (si no está guardada en disco), el recorrido aproximado y la distancia total.

---

## Comparación de Algoritmos

| Algoritmo                     | Complejidad Temporal | Calidad de la Solución | Uso de Memoria |
|-------------------------------|----------------------|------------------------|----------------|
| **Christofides**              | O(n^3)              | Aproximación 1.5x óptima | Alta           |
| **2-opt**                     | O(n^2) por iteración | Depende de la solución inicial | Baja           |
| **Vecino Más Cercano + Delta**| O(n^2)              | Heurística rápida, no garantiza óptimo | Baja           |
| **Híbrido (Vecino + 2-opt)**  | O(n^2) + O(n^2)     | Mejor que vecino más cercano, peor que Christofides | Media          |
| **Matriz de Distancias (C++ y Python)** | O(n^2) en paralelo | Depende del enfoque posterior (MST) | Media          |

---

## Instrucciones de Uso

1. **Preparación del Archivo TSP**:
   - Asegúrate de que el archivo TSP esté en el formato correcto. Los algoritmos esperan que las coordenadas de las ciudades estén en la sección `NODE_COORD_SECTION`.

2. **Ejecución**:
   - Ejecuta el script correspondiente al algoritmo que deseas probar. Por ejemplo:
     ```bash
     python christofides_algorithm.py
     ```

3. **Resultados**:
   - Cada script imprimirá el recorrido encontrado y, en algunos casos, métricas adicionales como la distancia total, el delta o el tiempo de ejecución.


## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.
