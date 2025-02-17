#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <cmath>
#include <limits>
#include <chrono>
#include <algorithm>

using namespace std;
using namespace std::chrono;

struct City {
    double x, y;
};

// TSP-file & user designed limited city

vector<City> leer_instancia_tsp(const string& archivo, int num_ciudades) {
    ifstream file(archivo);
    string line;
    vector<City> coordenadas;
    bool leer_coordenadas = false;

    while (getline(file, line)) {
        if (line.find("NODE_COORD_SECTION") != string::npos) {
            leer_coordenadas = true;
            continue;
        }
        if (line.find("EOF") != string::npos) break;

        if (leer_coordenadas && coordenadas.size() < num_ciudades) {
            stringstream ss(line);
            int id;
            double x, y;
            ss >> id >> x >> y;
            coordenadas.push_back({x, y});
        }
    }

    return coordenadas;
}

// Distance matrix

vector<vector<double>> calcular_distancias(const vector<City>& coordenadas) {
    int n = coordenadas.size();
    vector<vector<double>> distancias(n, vector<double>(n, 0.0));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i != j) {
                double dx = coordenadas[i].x - coordenadas[j].x;
                double dy = coordenadas[i].y - coordenadas[j].y;
                distancias[i][j] = sqrt(dx * dx + dy * dy);
            }
        }
    }

    return distancias;
}

// NN heuristic

vector<int> vecino_mas_cercano(const vector<City>& coordenadas, const vector<vector<double>>& distancias) {
    int n = coordenadas.size();
    if (n == 0) {
        cerr << "Error: No cities loaded!" << endl;
        exit(EXIT_FAILURE);
    }

    vector<bool> visitado(n, false);
    vector<int> ruta;
    
    int ciudad_actual = 0;
    ruta.push_back(ciudad_actual);
    visitado[ciudad_actual] = true;

    for (int i = 1; i < n; i++) {
        double min_dist = numeric_limits<double>::max();
        int ciudad_mas_cercana = -1;

        for (int j = 0; j < n; j++) {
            if (!visitado[j] && distancias[ciudad_actual][j] < min_dist) {
                min_dist = distancias[ciudad_actual][j];
                ciudad_mas_cercana = j;
            }
        }

        // NC valid
        
        if (ciudad_mas_cercana == -1) {
            cerr << "Error: No unvisited cities found!" << endl;
            exit(EXIT_FAILURE);
        }

        ciudad_actual = ciudad_mas_cercana;
        ruta.push_back(ciudad_actual);
        visitado[ciudad_actual] = true;
    }

    return ruta;
}


// TRD

double calcular_distancia_total(const vector<int>& ruta, const vector<vector<double>>& distancias) {
    double distancia_total = 0.0;
    int n = ruta.size();

    for (int i = 0; i < n - 1; i++)
        distancia_total += distancias[ruta[i]][ruta[i + 1]];
    
    distancia_total += distancias[ruta[n - 1]][ruta[0]];
    return distancia_total;
}

// 2-opt local optimization

vector<int> two_opt(vector<int> ruta, const vector<vector<double>>& distancias, int max_iteraciones = 100) {
    int n = ruta.size();
    bool mejora = true;

    for (int iter = 0; iter < max_iteraciones && mejora; iter++) {
        mejora = false;
        for (int i = 1; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (j - i == 1) continue;

                double delta = (distancias[ruta[i-1]][ruta[j]] + distancias[ruta[i]][ruta[j+1]]) -
                               (distancias[ruta[i-1]][ruta[i]] + distancias[ruta[j]][ruta[j+1]]);
                
                if (delta < 0) {
                    reverse(ruta.begin() + i, ruta.begin() + j + 1);
                    mejora = true;
                }
            }
        }
    }

    return ruta;
}

vector<City> leer_instancia_tsp(const string& archivo) {
    ifstream file(archivo);
    
    if (!file) {
        cerr << "Error: Could not open file " << archivo << endl;
        exit(EXIT_FAILURE);
    }

    string line;
    vector<City> coordenadas;
    bool leer_coordenadas = false;

    while (getline(file, line)) {
        if (line.find("NODE_COORD_SECTION") != string::npos) {
            leer_coordenadas = true;
            continue;
        }
        if (line.find("EOF") != string::npos) break;

        if (leer_coordenadas) {
            stringstream ss(line);
            int id;
            double x, y;
            ss >> id >> x >> y;
            if (ss.fail()) continue; // Skip invalid lines
            coordenadas.push_back({x, y});
        }
    }

    if (coordenadas.empty()) {
        cerr << "Error: No cities found in file!" << endl;
        exit(EXIT_FAILURE);
    }

    return coordenadas;
}

// Main 

int main() {
    string archivo_tsp = "pla33810.tsp";  // TSP updates
    int num_ciudades;

    cout << "Ingrese el número de ciudades a considerar: ";
    cin >> num_ciudades;

    vector<City> coordenadas = leer_instancia_tsp(archivo_tsp, num_ciudades);
    vector<vector<double>> distancias = calcular_distancias(coordenadas);

    auto start = high_resolution_clock::now();
    vector<int> ruta = vecino_mas_cercano(coordenadas, distancias);
    double distancia_inicial = calcular_distancia_total(ruta, distancias);
    auto stop = high_resolution_clock::now();
    cout << "Distancia inicial: " << distancia_inicial << endl;
    cout << "Tiempo Nearest Neighbor: " << duration<double>(stop - start).count() << "s\n";

    start = high_resolution_clock::now();
    ruta = two_opt(ruta, distancias);
    double distancia_optima = calcular_distancia_total(ruta, distancias);
    stop = high_resolution_clock::now();
    cout << "Distancia optimizada: " << distancia_optima << endl;
    cout << "Tiempo 2-opt: " << duration<double>(stop - start).count() << "s\n";

    return 0;
}
