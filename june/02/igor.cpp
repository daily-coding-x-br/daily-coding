#include <bits/stdc++.h>
using namespace std;

int mat[1001][1001];
string s1, s2;

int dp(int i, int j) {
    if (mat[i][j] != -1) return mat[i][j];

    int r = 0x3f3f3f3f;
    if (i == (int) s1.length() && j == (int) s2.length()) r = 0;
    else if (i == (int) s1.length()) r = s2.length() - j;
    else if (j == (int) s2.length()) r = s1.length() - i;
    else {
        if (s1[i] == s2[j])
            r = min(r, dp(i+1, j+1));
        else r = min(r, 1+dp(i+1, j+1));
        r = min(r, 1+dp(i+1, j));
        r = min(r, 1+dp(i, j+1));
    }
    
    mat[i][j] = r;
    return r;
}

int main() {
    cin >> s1 >> s2;
    memset(mat, -1, sizeof(mat));
    cout << dp(0, 0) << endl;
    return 0;
}
