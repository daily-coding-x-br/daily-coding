#include <bits/stdc++.h>
using namespace std;

bool mat[1000][1000];
bool visited[1000][1000];
int n, m;

int main() {
    int i1, j1, i2, j2;
    cin >> n >> m >> i1 >> j1 >> i2 >> j2;
    char c;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) {
            cin >> c;
            mat[i][j] = (c == 't');
        }

    queue<pair<pair<int, int>, int>> q;
    q.push({{i1, j1}, 0});
    visited[i1][j1] = true;
    int r = -1;
    while (!q.empty()) {
        int i = q.front().first.first, j = q.front().first.second;
        int s = q.front().second;
        q.pop();
        if (i == i2 && j == j2) { r = s; break; }

        if (i > 0 && !visited[i-1][j] && mat[i-1][j] == false) q.push({{i-1, j}, s+1});
        if (i < n-1 && !visited[i+1][j] && mat[i+1][j] == false) q.push({{i+1, j}, s+1});
        if (j > 0 && !visited[i][j-1] && mat[i][j-1] == false) q.push({{i, j-1}, s+1});
        if (j < m-1 && !visited[i][j+1] && mat[i][j+1] == false) q.push({{i, j+1}, s+1});
    }
    cout << r << endl;
    return 0;
}
