#include <iostream>
#include <vector>
#include <limits>

using namespace std;

const int INF = numeric_limits<int>::max() / 2; // Prevent overflow

// Function to count Hamiltonian cycles using bitmask DP (FSA-based approach)
int countHamiltonianCycles(int n, vector<vector<int>> &graph) {
    vector<vector<int>> dp(1 << n, vector<int>(n, 0));
    dp[1][0] = 1;  // Start from city 0
    
    for (int mask = 1; mask < (1 << n); ++mask) {
        for (int u = 0; u < n; ++u) {
            if (!(mask & (1 << u))) continue;  // Skip if u is not in the set
            for (int v = 0; v < n; ++v) {
                if ((mask & (1 << v)) || graph[u][v] == INF) continue;
                dp[mask | (1 << v)][v] += dp[mask][u];
            }
        }
    }
    
    int cycleCount = 0;
    for (int u = 1; u < n; ++u) {
        if (graph[u][0] != INF) {
            cycleCount += max(0, dp[(1 << n) - 1][u]);  // Ensure non-negative count
        }
    }
    return cycleCount;
}

// Function to find the shortest Hamiltonian cycle
int shortestHamiltonianCycle(int n, vector<vector<int>> &graph) {
    vector<vector<int>> dp(1 << n, vector<int>(n, INF));
    dp[1][0] = 0;
    
    for (int mask = 1; mask < (1 << n); ++mask) {
        for (int u = 0; u < n; ++u) {
            if (!(mask & (1 << u))) continue;
            for (int v = 0; v < n; ++v) {
                if ((mask & (1 << v)) || graph[u][v] == INF) continue;
                dp[mask | (1 << v)][v] = min(dp[mask | (1 << v)][v], dp[mask][u] + graph[u][v]);
            }
        }
    }
    
    int minCycle = INF;
    for (int u = 1; u < n; ++u) {
        if (graph[u][0] != INF) {
            minCycle = min(minCycle, dp[(1 << n) - 1][u] + graph[u][0]);
        }
    }
    return (minCycle >= INF) ? -1 : minCycle; // Ensure valid output
}

int main() {
    int n;
    cout << "Enter number of cities: ";
    cin >> n;
    
    vector<vector<int>> graph(n, vector<int>(n, INF));
    cout << "Enter adjacency matrix (use INF for no path):" << endl;
    
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> graph[i][j];
            if (i == j) graph[i][j] = INF; // No self-loops
        }
    }
    
    int hamiltonianCycles = countHamiltonianCycles(n, graph);
    int shortestCycle = shortestHamiltonianCycle(n, graph);
    
    cout << "Total Hamiltonian Cycles: " << hamiltonianCycles << endl;
    cout << "Shortest Hamiltonian Cycle Length: " << shortestCycle << endl;
    
    return 0;
}
