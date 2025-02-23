#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>

extern "C" {
    void calculate_distance_matrix(double* cities, int num_cities, double* distance_matrix) {
        for (int i = 0; i < num_cities; i++) {
            for (int j = 0; j < num_cities; j++) {
                double dx = cities[i * 2] - cities[j * 2];
                double dy = cities[i * 2 + 1] - cities[j * 2 + 1];
                distance_matrix[i * num_cities + j] = std::sqrt(dx * dx + dy * dy);
            }
        }
    }
}
