// Swapping array elements to make v[i] = i when possible, then finding first i
// such that v[i] != i
#include <bits/stdc++.h>
using namespace std;


int main() {
    int n, x;
    vector<int> v;
    cin >> n;
    v.push_back(0);
    for (int i = 1; i <= n; i++) {
        cin >> x;
        v.push_back(x);
    }

    int aux;
    for (int i = 1; i <= n; i++)
        while (0 < v[i] && v[i] <= n && v[v[i]] != v[i]) {
            aux = v[i];
            v[i] = v[aux];
            v[aux] = aux;
        }

    for (int i = 1; i <= n; i++)
        if (v[i] != i) { cout << i << endl; break; } 

    return 0;
}
