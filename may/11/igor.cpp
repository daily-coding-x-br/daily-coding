#include <bits/stdc++.h>
using namespace std;

int max_nonadj(vector<int> &v) {
    int a = 0, b = v[0], c;
    for (int i = 2; i < (int) v.size(); i++) {
        c = b;
        b = max(a + v[i], b);
        a = c;
    }

    return b;
}

int main() {
    int n, x;
    vector<int> v;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> x;
        v.push_back(x);
    }
    cout << max_nonadj(v) << endl;

    return 0;
}
