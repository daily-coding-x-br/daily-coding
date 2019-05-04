#include <bits/stdc++.h>
using namespace std;

bool findSumLog(vector<int> &v, int k) {
    sort(v.begin(), v.end());
    int a = 0, b = v.size()-1;

    while (a < b) {
        if (v[a] + v[b] > k) b--;
        else if (v[a] + v[b] < k) a++;
        else return true;
    }
    return false;
}

int main() {
    int n, k, x;
    vector<int> v;
    cin >> n >> k;
    for (int i = 0; i < n; i++) {
        cin >> x;
        v.push_back(x);
    }

    cout << findSumLog(v, k) << endl;
    return 0;
}
