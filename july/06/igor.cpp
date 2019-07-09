#include <bits/stdc++.h>
using namespace std;

void printSpiral(vector<vector<int>> &mat) {
    int n = mat.size();
    int m = mat[0].size();
    int i = 0, j = 0;
    int tot = 0;
    int lm = 0, rm = 0, tm = 1, bm = 0;
    int state = 0; // 0 -> going right, 1 -> going down, 2 -> going left
    
    while (tot != n * m) {
        cout << mat[i][j] << endl;
        tot++;
        if (state == 0) {
            if (j+1 < m-rm) j++;
            else { i++; state = 1; rm++; }
        } else if (state == 1) {
            if (i+1 < n-bm) i++;
            else { j--; state = 2; bm++; }
        } else if (state == 2) {
            if (j-1 >= lm) j--;
            else { i--; state = 3; lm++; }
        } else {
            if (i-1 >= tm) i--;
            else { j++; state = 0; tm++; }
        }
    }
}

int main() {
    vector<vector<int>> m;
    m.push_back({1, 2, 3, 4, 5});
    m.push_back({6, 7, 8, 9, 10});
    m.push_back({11, 12, 13, 14, 15});
    m.push_back({16, 17, 18, 19, 20});
    printSpiral(m);
    return 0;
}
