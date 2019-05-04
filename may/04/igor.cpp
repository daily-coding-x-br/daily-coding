// O(n), com 3 vetores auxiliares. Fazendo a multiplicacao indo e voltando no 
// vetor, depois eh soh multiplicar os valores de cada lado
#include <bits/stdc++.h>
using namespace std;

vector<int> multOthers(vector<int> &v) {
    int n = v.size();
    vector<int> a, b, res;
    a.assign(n, 1); b.assign(n, 1);
    int x = 1;
    for (int i = 0; i < n; i++)
        a[i] = x *= v[i];
    x = 1;
    for (int i = n-1; i >= 0; i--)
        b[i] = x *= v[i];

    res.assign(n, 1);
    for (int i = 0; i < n; i++) {
        if (i > 0) res[i] *= a[i-1];
        if (i < n-1) res[i] *= b[i+1];
    }
    return res;
}

int main() {
    int n, x;
    vector<int> v;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> x;
        v.push_back(x);
    }

    v = multOthers(v);
    for (int i = 0; i < n; i++)
        cout << v[i] << " ";
    cout << endl;
    return 0;
}
