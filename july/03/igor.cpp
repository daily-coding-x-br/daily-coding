#include <bits/stdc++.h>
using namespace std;

int count(int n, int m) {
    vector<vector<int>> ma;
    ma.assign(n, {});
    for (int i = 0; i < n; i++)
        ma[i].assign(m, 0);

    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {
            if (i == 0 || j == 0) ma[i][j] = 1;
            else ma[i][j] = ma[i-1][j] + ma[i][j-1];
        }
    return ma[n-1][m-1];
}

int main() {
    cout << count(5, 5) << endl;
    return 0;
}
