// Greedy algorithm, O(V^2)
#include <bits/stdc++.h>
using namespace std;

class Graph {
private:
    bool m[1001][1001];
    int n;

public:
    Graph(int n) {
        this->n = n;
    }

    void addEdge(int a, int b) {
        m[a][b] = true;
        m[b][a] = true;
    }

    int canColor(int k) {
        queue<int> q;
        int colors[1001] = {0};
        bool used[1001] = {0};
        q.push(1);
        while (!q.empty()) {
            int cur = q.front();
            q.pop();
            if (colors[cur] != 0) continue;
            memset(used, 0, n * sizeof(bool));
            for (int j = 1; j <= n; j++)
                if (m[cur][j]) {
                    if (colors[j] != 0)
                        used[colors[j]] = true;
                    else q.push(j);
                }
            for (int i = 1; i <= k; i++)
                if (used[i] == 0) {
                    colors[cur] = i; 
                    break;
                }
            if (colors[cur] == 0) return false;
        }
        for (int i = 1; i <= n; i++)
            cout << colors[i] << " ";
        cout << endl;
        return true;
    }
};

int main() {
    Graph g(5);
    g.addEdge(1, 2);
    g.addEdge(1, 3);
    g.addEdge(2, 3);
    g.addEdge(2, 5);
    g.addEdge(3, 4);
    g.addEdge(4, 5);
    cout << g.canColor(2) << endl;
    cout << g.canColor(3) << endl;
    cout << g.canColor(4) << endl;
    return 0;
}
