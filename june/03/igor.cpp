// Changing values to the negative logs, then using bellman-ford to 
// identify negative sums.
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, x;
    vector<vector<double>> m;
    vector<double> min_dist;

    cin >> n;
    for (int i = 0; i < n; i++) {
        m.push_back({});
        min_dist.push_back(DBL_MAX);
        for (int j = 0; j < n; j++) {
            cin >> x;
            m[i].push_back(-log(x));
        }
    }

    bool arb = false;
    int source = 0;
    min_dist[source] = 0;
    for (int i = 0; i < n-1 && !arb; i++) {
        for (int u = 0; u < n; u++)
            for (int v = 0; v < n; v++)
                min_dist[v] = min(min_dist[v], min_dist[u] + m[u][v]);

        for (int u = 0; u < n; u++)
            for (int v = 0; v < n; v++)
                if (min_dist[v] > min_dist[u] + m[u][v])
                    arb = true;
    }

    cout << arb << endl;
    return 0;
}
