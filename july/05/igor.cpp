#include <bits/stdc++.h>
using namespace std;

bool visited[20][20];
int nVisited;
int stepI[] = {1, 1, 2, 2, -1, -1, -2, -2};
int stepJ[] = {2, -2, 1, -1, 2, -2, 1, -1};

int tours(int i, int j, int n) {
    int r = 0;
    for (int k = 0; k < 8; k++) {
        int is = i + stepI[k];
        int js = j + stepJ[k];
        if (0 <= is && is < n && 0 <= js && js < n && !visited[is][js]) {
            nVisited++;
            visited[is][js] = true;
            if (nVisited == n*n) r += 1;
            else r += tours(is, js, n);
            visited[is][js] = false;
            nVisited--;
        }
    }
    return r;
}

int countTours(int n) {
    int r = 0;
    nVisited = 1;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) {
            visited[i][j] = true;
            r += tours(i, j, n);
            visited[i][j] = false;
        }
    return r;
}

int main() {
    cout << countTours(5) << endl;
    return 0;
}
