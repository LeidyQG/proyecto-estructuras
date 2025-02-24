# README: CC - Delta TSP Solver
------------------------README -----------------GUI------------------------------------------------------------------------------------  
## Descripción General

El CC - Delta TSP Solver es una aplicación gráfica diseñada para resolver instancias del problema del Viajante de Comercio (TSP, por sus siglas en inglés). La aplicación está construida utilizando la biblioteca `tkinter` de Python, con extensiones de `tkinterdnd2` para soportar la funcionalidad de arrastrar y soltar archivos. La interfaz gráfica está organizada en varias secciones que permiten al usuario cargar archivos de instancias TSP, procesarlos utilizando diferentes algoritmos y visualizar los resultados.

## Estructura del Proyecto

El proyecto está organizado en varios módulos y archivos que gestionan diferentes aspectos de la interfaz gráfica y la lógica de la aplicación. A continuación, se describe la estructura y funcionalidad de cada uno de los archivos proporcionados:

### 1. `gui.py`

Este archivo contiene la clase principal `GUI`, que gestiona la ventana principal de la aplicación y organiza los diferentes marcos (frames) en una estructura de pestañas (`Notebook`). Los marcos principales son:

- **Frame_Load**: Para cargar archivos TSP.
- **Frame_Process**: Para procesar el archivo cargado utilizando diferentes algoritmos.
- **Frame_Results**: Para visualizar los resultados del procesamiento.

La clase `GUI` también maneja el estilo de la ventana principal, incluyendo su tamaño y posición en la pantalla.

### 2. `custom_widgets.py`

Este archivo define la clase `WindowAppTools`, que proporciona utilidades comunes para la creación de widgets personalizados. Incluye métodos para calcular porcentajes de la ventana, obtener rutas de iconos y crear botones y títulos personalizados.

### 3. `frame_load.py`

Este archivo define la clase `Frame_Load`, que gestiona la interfaz para cargar archivos TSP. Permite al usuario cargar un archivo mediante un diálogo de selección de archivos o arrastrando y soltando el archivo en la ventana. También incluye una sección para descargar archivos TSP de ejemplo.

### 4. `frame_process.py`

Este archivo define la clase `Frame_Process`, que gestiona la interfaz para procesar el archivo TSP cargado. Incluye una sección para previsualizar el contenido del archivo y una lista de algoritmos disponibles para procesar el archivo. Los algoritmos se presentan como botones que el usuario puede seleccionar.

### 5. `frame_results.py`

Este archivo define la clase `Frame_Results`, que gestiona la interfaz para visualizar los resultados del procesamiento. Actualmente, esta sección está en desarrollo y solo muestra un título.

### 6. `app_globals.py`

- **Variables Globales**:
  - `file_loaded`: Indica si un archivo TSP ha sido cargado.
  - `file_previewed`: Indica si el archivo cargado ha sido previsualizado.
  - `file_processed`: Indica si el archivo ha sido procesado.
  - `file_graphed`: Indica si los resultados del procesamiento han sido graficados.
  - `file_path`: Almacena la ruta del archivo TSP cargado.

- **Funciones**:
  - `get_file_loaded()`, `get_file_previewed()`, `get_file_processed()`, `get_file_graphed()`: Devuelven el estado actual de las variables globales correspondientes.
  - `set_file_loaded()`, `set_file_previewed()`, `set_file_processed()`, `set_file_graphed()`: Establecen el estado de las variables globales y, en algunos casos, generan eventos para actualizar la interfaz gráfica.
  - `get_file_path()`: Devuelve la ruta del archivo cargado.
  - `set_file_path()`: Establece la ruta del archivo y actualiza el estado de la aplicación en consecuencia.


### 7. `file_utils.py`

Este archivo contiene funciones utilitarias para manejar la interacción con archivos, específicamente para la funcionalidad de arrastrar y soltar archivos y para cargar el contenido de un archivo en un búfer.

- **Funciones**:
  - `handle_file_drop(file_drop_event: DnDEvent, parent: Misc)`: Maneja el evento de arrastrar y soltar un archivo en la ventana de la aplicación. Verifica que el archivo sea válido y actualiza el estado global de la aplicación.
  - `load_file_contents_buffer(file_path: pathlib.Path)`: Carga el contenido de un archivo en un búfer de texto y lo devuelve como una cadena. Esta función se utiliza para previsualizar el contenido del archivo TSP en la interfaz gráfica.

## Instalación y Ejecución

Para ejecutar la aplicación, asegúrate de tener instaladas las siguientes dependencias:

- Python 3.x
- `tkinter` (generalmente incluido con Python)
- `tkinterdnd2` (para soportar arrastrar y soltar archivos)

Puedes instalar `tkinterdnd2` utilizando pip:

```bash
pip install tkinterdnd2
```

Una vez instaladas las dependencias, puedes ejecutar la aplicación ejecutando el archivo principal `gui.py`:

```bash
python gui.py
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
----------------------------------------------------------------FIN--------README---------GUI-------------------
     -------------------------------------README-----------ALGORITMOS-------------------------
# README: Implementaciones de Algoritmos para el Problema del Viajante de Comercio (TSP)

Este repositorio contiene cinco implementaciones de algoritmos para resolver el Problema del Viajante de Comercio (TSP). Cada algoritmo tiene su propio enfoque y características, lo que permite comparar su rendimiento y resultados. A continuación, se describe cada uno de los algoritmos y su funcionamiento.

---

## 1. **Algoritmo de Christofides**

### Descripción
El algoritmo de Christofides es una aproximación clásica para resolver el TSP. Combina un Árbol de Expansión Mínima (MST) con un emparejamiento perfecto de peso mínimo para construir un circuito euleriano, que luego se convierte en un circuito hamiltoniano.

### Archivo: `christofides_algorithm.py`

#### Funciones Principales:
- **`load_tsp_instance(file_path)`**: Lee un archivo TSP y extrae las coordenadas de las ciudades.
- **`calculate_distance_matrix(coordinates)`**: Calcula la matriz de distancias entre las ciudades.
- **`minimum_spanning_tree(graph)`**: Construye un Árbol de Expansión Mínima (MST) a partir de la matriz de distancias.
- **`odd_degree_vertices(mst)`**: Encuentra los vértices de grado impar en el MST.
- **`eulerian_circuit(graph, start)`**: Encuentra un circuito euleriano en el grafo.
- **`christofides_algorithm(graph)`**: Implementa el algoritmo de Christofides para encontrar una solución aproximada al TSP.

#### Ejecución:
```bash
python christofides_algorithm.py
```

#### Resultados:
- Imprime el recorrido (tour) encontrado por el algoritmo.

---

## 2. **Algoritmo 2-opt**

### Descripción
El algoritmo 2-opt es una técnica de optimización local que mejora una solución inicial (por ejemplo, un tour aleatorio) intercambiando pares de aristas para reducir la distancia total del recorrido.

### Archivo: `2_opt_algorithm.py`

#### Funciones Principales:
- **`read_tsp_file(filename)`**: Lee un archivo TSP y extrae las coordenadas de las ciudades.
- **`calculate_distance(point1, point2)`**: Calcula la distancia euclidiana entre dos puntos.
- **`total_distance(tour, coords)`**: Calcula la distancia total de un recorrido.
- **`two_opt(tour, coords)`**: Aplica el algoritmo 2-opt para optimizar un recorrido.
- **`generate_initial_tour(num_cities)`**: Genera un recorrido inicial aleatorio.
- **`delta_tsp(filename)`**: Implementa el algoritmo 2-opt para resolver el TSP.

#### Ejecución:
```bash
python 2_opt_algorithm.py
```

#### Resultados:
- Imprime el recorrido optimizado y la distancia total.

---

## 3. **Algoritmo del Vecino Más Cercano con Delta**

### Descripción
Este algoritmo utiliza la heurística del vecino más cercano para construir un recorrido inicial y luego calcula el delta (diferencia entre la arista más larga y la más corta) como métrica de calidad.

### Archivo: `nearest_neighbor_delta.py`

#### Funciones Principales:
- **`leer_instancia_tsp(archivo)`**: Lee un archivo TSP y extrae las coordenadas de las ciudades.
- **`delta_tsp_vecino_mas_cercano(coordenadas)`**: Implementa el algoritmo del vecino más cercano y calcula el delta.
- **`main(archivo_tsp)`**: Función principal que ejecuta el algoritmo y muestra los resultados.

#### Ejecución:
```bash
python nearest_neighbor_delta.py
```

#### Resultados:
- Imprime el recorrido encontrado, el delta y el tiempo de ejecución.

---

## 4. **Algoritmo Híbrido: Vecino Más Cercano + 2-opt**

### Descripción
Este algoritmo combina la heurística del vecino más cercano para generar una solución inicial y luego aplica el algoritmo 2-opt para optimizar el recorrido.

### Archivo: `hybrid_nearest_neighbor_2opt.py`

#### Funciones Principales:
- **`leer_instancia_tsp(archivo)`**: Lee un archivo TSP y extrae las coordenadas de las ciudades.
- **`vecino_mas_cercano(coordenadas, distancias)`**: Implementa el algoritmo del vecino más cercano.
- **`calcular_distancia_total(ruta, distancias)`**: Calcula la distancia total de un recorrido.
- **`two_opt(ruta, distancias, max_iteraciones=100)`**: Aplica el algoritmo 2-opt para optimizar un recorrido.
- **`main(archivo_tsp)`**: Función principal que ejecuta el algoritmo híbrido y muestra los resultados.

#### Ejecución:
```bash
python hybrid_nearest_neighbor_2opt.py
```

#### Resultados:
- Imprime la distancia inicial (vecino más cercano), la distancia optimizada (2-opt) y los tiempos de ejecución.

---

## 5. **Algoritmo de Cálculo de Matriz de Distancias en Paralelo (C++ y Python)**

### Descripción
Este algoritmo utiliza una implementación en C++ para calcular la matriz de distancias entre ciudades en paralelo, lo que mejora significativamente el rendimiento en comparación con una implementación secuencial. Luego, utiliza un enfoque basado en el Árbol de Expansión Mínima (MST) para aproximar una solución al TSP.

### Archivos:
- **`tsp_solver.py`**: Script en Python que utiliza la biblioteca compartida en C++ para calcular la matriz de distancias y aproximar una solución al TSP.
- **`distance_calculator.cpp`**: Implementación en C++ del cálculo de la matriz de distancias en paralelo.

#### Funciones Principales (Python):
- **`read_tsp_file(file_path)`**: Lee un archivo TSP y extrae las coordenadas de las ciudades.
- **`calculate_distance_matrix_parallel(cities, num_threads=4)`**: Calcula la matriz de distancias en paralelo utilizando la biblioteca compartida en C++.
- **`mst_approximation_tsp(distance_matrix)`**: Aproxima una solución al TSP utilizando el MST.
- **`calculate_tour_distance(tour, distance_matrix)`**: Calcula la distancia total de un recorrido.
- **`main(file_path, num_threads=4)`**: Función principal que ejecuta el algoritmo y muestra los resultados.

#### Funciones Principales (C++):
- **`calculate_distance_block(const double* cities, int num_cities, double* distance_matrix, int start, int end)`**: Calcula las distancias para un bloque de ciudades.
- **`calculate_distance_matrix(double* cities, int num_cities, double* distance_matrix, int num_threads)`**: Función principal que divide el trabajo entre múltiples hilos para calcular la matriz de distancias en paralelo.

#### Ejecución:
1. Compila el archivo C++:
   ```bash
   g++ -shared -o distance_calculator.so -fPIC distance_calculator.cpp -lpthread
   ```
2. Ejecuta el script de Python:
   ```bash
   python tsp_solver.py
   ```

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
