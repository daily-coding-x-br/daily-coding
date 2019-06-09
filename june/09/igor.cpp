// Backtracking, O(n^n)
#include <bits/stdc++.h>
using namespace std;

int n;
bool usedC[100];
bool usedDr[201];
bool usedDl[201];

int nQueens(int i) {
    if (i == n) return 1;

    int tot = 0;
    for (int j = 0; j < n; j++) {
        if (!usedC[j] && !usedDr[i-j+n] && !usedDl[i+j]) {
            usedC[j] = true;
            usedDr[i-j+n] = true;
            usedDl[i+j] = true;
            tot += nQueens(i+1);
            usedC[j] = false;
            usedDr[i-j+n] = false;
            usedDl[i+j] = false;
       }
    }

    return tot;
}

int main() {
    cin >> n;
    cout << nQueens(0) << endl;
    return 0;
}
