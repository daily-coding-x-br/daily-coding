// Memoization, O(n*k)
#include <bits/stdc++.h>
using namespace std;

int n, k, x;
vector<int> v, chosen;
vector<vector<bool>> tried;

bool dp(int i, int s) {
    if (s == k) return true;
    if (i >= n || s > k) return false;
    if (tried[i][s]) return false;

    chosen.push_back(v[i]);
    if (dp(i+1, s+v[i])) return true;
    chosen.pop_back();
    if (dp(i+1, s)) return true;
    tried[i][s] = true;
    return false;
}

int main() {
    cin >> n >> k;
    tried.assign(n, {});
    for (int i = 0; i < n; i++) {
        cin >> x;
        v.push_back(x);
        tried[i].assign(k, 0);
    }

    if (dp(0, 0)) {
        for (auto k : chosen)
            cout << k << " ";
        cout << endl;
    } else cout << "NULL" << endl;

    return 0;
}
