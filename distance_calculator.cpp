#include <iostream>
#include <vector>
#include <cmath>
#include <thread>
#include <mutex>

// Mutex para proteger el acceso a la matriz de distancias
std::mutex mtx;

// Función para calcular las distancias de un bloque de ciudades
void calculate_distance_block(const double* cities, int num_cities, double* distance_matrix, int start, int end) {
    for (int i = start; i < end; i++) {
        for (int j = 0; j < num_cities; j++) {
            double dx = cities[i * 2] - cities[j * 2];
            double dy = cities[i * 2 + 1] - cities[j * 2 + 1];
            double distance = std::sqrt(dx * dx + dy * dy);

            // Usar mutex para evitar condiciones de carrera
            std::lock_guard<std::mutex> lock(mtx);
            distance_matrix[i * num_cities + j] = distance;
        }
    }
}

// Función principal para calcular la matriz de distancias en paralelo
extern "C" {
    void calculate_distance_matrix(double* cities, int num_cities, double* distance_matrix, int num_threads) {
        std::vector<std::thread> threads;
        int block_size = num_cities / num_threads;

        // Crear y lanzar los hilos
        for (int i = 0; i < num_threads; i++) {
            int start = i * block_size;
            int end = (i == num_threads - 1) ? num_cities : start + block_size;
            threads.emplace_back(calculate_distance_block, cities, num_cities, distance_matrix, start, end);
        }

        // Esperar a que todos los hilos terminen
        for (auto& thread : threads) {
            thread.join();
        }
    }
}
