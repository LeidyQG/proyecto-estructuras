#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <limits>

using namespace std;

const int INF = numeric_limits<int>::max() / 2;

vector<vector<int>> parseTSPLibToAdjMatrix(const string &filename) {
    ifstream file(filename);
    if (!file) {
        cerr << "Error opening file!" << endl;
        exit(EXIT_FAILURE);
    }

    string line;
    int dimension = 0;
    vector<vector<int>> matrix;
    bool readingWeights = false;
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
        } else if (readingWeights) {
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
            if (row >= dimension) break; // Stop reading if all data is processed
        }
    }
    file.close();
    return matrix;
}

int main() {
    string filename = "ulysses22.opt.tour"; // Change this as needed
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
