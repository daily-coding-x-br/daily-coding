// Representing in a matrix
#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<vector<bool>> mat;
vector<vector<bool>> aux;

void resize(int n, int m) {
    while ((int) aux.size() < n) {
        aux.push_back({});
        aux.back().assign(aux[0].size(), 0);
    }
    while ((int) aux[0].size() < m) {
        for (auto &v : aux)
            v.push_back(0);
    }

    while ((int) mat.size() < n) {
        mat.push_back({});
        mat.back().assign(mat[0].size(), 0);
    }
    while ((int) mat[0].size() < m) {
        for (auto &v : mat)
            v.push_back(0);
    }
}

void update() {
    bool moveDown = false, moveRight = false;
    for (int j = 1; j < m-1; j++)
        if (mat[0][j-1] && mat[0][j] && mat[0][j+1]) {
            moveDown = true;
            aux[0][j] = true;
        }
    for (int i = 1; i < n-1; i++)
        if (mat[i-1][0] && mat[i][0] && mat[i+1][0]) {
            moveRight = true;
            aux[i][0] = true;
        }

    resize(n+moveDown+1, m+moveRight+1);

    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {
            int alive = 0;    
            if (i > 0 && mat[i-1][j]) alive++;
            if (i < n-1 && mat[i+1][j]) alive++;
            if (j > 0 && mat[i][j-1]) alive++;
            if (j < m-1 && mat[i][j+1]) alive++;
            if (i > 0 && j > 0 && mat[i-1][j-1]) alive++;
            if (i > 0 && j < m-1 && mat[i-1][j+1]) alive++;
            if (i < n-1 && j > 0 && mat[i+1][j-1]) alive++;
            if (i < n-1 && j < m-1 && mat[i+1][j+1]) alive++;

            if (mat[i][j] && (alive == 2 || alive == 3))
                aux[i+moveDown][j+moveRight] = true;
            if (!mat[i][j] && alive == 3)
                aux[i+moveDown][j+moveRight] = true;
        }

    bool incN = false, incM = false;
    for (int j = 1; j < m-1; j++)
        if (mat[n-1][j-1] && mat[n-1][j] && mat[n-1][j+1]) {
            aux[n+moveDown][j+moveRight] = true;
            incN = true;
        }
    for (int i = 1; i < n-1; i++)
        if (mat[i-1][m-1] && mat[i][m-1] && mat[i+1][m-1]) {
            aux[i+moveDown][m+moveRight] = true;
            incM = true;
        }

    n += moveDown;
    n += incN;
    m += moveRight;
    m += incM;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {
            mat[i][j] = aux[i][j];
            aux[i][j] = 0;
        }
}

void print() {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++)
            cout << (mat[i][j] ? '*' : '.');
        cout << endl;
    }
    cout << endl;
}

int main() {
    int p, t;
    vector<pair<int, int>> input;
    cin >> p >> t;
    input.reserve(p);
    while (p--) {
        int x, y;
        cin >> x >> y;
        input.push_back({x, y});
        n = max(n, x);
        m = max(m, y);
    }
    n++;
    m++;

    mat.assign(n, {});
    aux.assign(n, {});
    for (int i = 0; i < n; i++) {
        mat[i].assign(m, 0);
        aux[i].assign(m, 0);
    }
    for (auto ip : input)
        mat[ip.first][ip.second] = true;

    print();
    while (t--) {
        update();
        print();
    }

    return 0;
}

