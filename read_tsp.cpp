#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <cmath>
#include <limits>

using namespace std;

const int INF = numeric_limits<int>::max() / 2;

struct Point {
    double x, y;
};

vector<vector<int>> parseTSPLibToAdjMatrix(const string &filename) {
    ifstream file(filename);
    if (!file) {
        cerr << "Error opening file!" << endl;
        exit(EXIT_FAILURE);
    }

    string line;
    int dimension = 0;
    vector<vector<int>> matrix;
    vector<Point> points;
    bool readingCoords = false, readingWeights = false;
    int row = 0, col = 0;

    while (getline(file, line)) {
        if (line.find("DIMENSION") != string::npos) {
            stringstream ss(line);
            string temp;
            ss >> temp >> temp >> dimension;
            matrix.assign(dimension, vector<int>(dimension, INF));
        } else if (line.find("EDGE_WEIGHT_SECTION") != string::npos) {
            readingWeights = true;
            row = 0;
            col = 0;
            continue;
        } else if (line.find("NODE_COORD_SECTION") != string::npos) {
            readingCoords = true;
            continue;
        } else if (line.find("EOF") != string::npos) {
            break;
        }

        if (readingWeights) {
            stringstream ss(line);
            int weight;
            while (ss >> weight) {
                if (row < dimension && col < dimension) {
                    matrix[row][col] = (weight == 0 ? INF : weight);
                    matrix[col][row] = matrix[row][col]; // Symmetric TSP
                    col++;
                    if (col == dimension) {
                        col = 0;
                        row++;
                    }
                }
            }
            if (row >= dimension) break;
        } else if (readingCoords) {
            stringstream ss(line);
            int index;
            double x, y;
            ss >> index >> x >> y;
            points.push_back({x, y});
        }
    }
    file.close();

    if (!points.empty()) {
        // Compute Euclidean distances
        for (int i = 0; i < dimension; i++) {
            for (int j = 0; j < dimension; j++) {
                if (i != j) {
                    double dx = points[i].x - points[j].x;
                    double dy = points[i].y - points[j].y;
                    matrix[i][j] = round(sqrt(dx * dx + dy * dy));
                }
            }
        }
    }

    return matrix;
}

int main() {
    string filename = "ulysses22.tsp"; // Change as needed
    vector<vector<int>> adjacencyMatrix = parseTSPLibToAdjMatrix(filename);
    
    cout << "Adjacency Matrix:" << endl;
    for (const auto &row : adjacencyMatrix) {
        for (int val : row) {
            cout << (val == INF ? "INF" : to_string(val)) << " ";
        }
        cout << endl;
    }
    return 0;
}
