// DP, O(n*m)
#include <bits/stdc++.h>
using namespace std;

int mat[1000][1000];

bool dp(int i, int j, string match, string s) {
    if (mat[i][j] != -1)
        return mat[i][j];

    bool ans;
    if (j == (int) s.length())
        ans = (i == (int) match.length());
    else {
        bool first_match = (i < (int) match.length() && 
                            (s[j] == match[i] || s[j] == '.'));

        if (j+1 < (int) s.length() && s[j+1] == '*')
            ans = (dp(i, j+2, match, s) || (first_match && dp(i+1, j, match, s)));
        else ans = first_match && dp(i+1, j+1, match, s);
    }
    mat[i][j] = ans;
    return ans;
}

int main() {
    string match, s;
    cin >> match >> s;
    memset(mat, -1, sizeof(int) * 1000000);
    cout << dp(0, 0, match, s) << endl;

    return 0;
}
