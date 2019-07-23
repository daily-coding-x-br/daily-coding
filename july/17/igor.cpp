// Dont think i got this, problem, just analyzing each column to see if it needs
// to be removed
#include <bits/stdc++.h>
using namespace std;

int nRemovals(vector<vector<char>> m) {
    if (m.empty()) return 0;

    int n = 0;
    for (int j = 0; j < (int) m[0].size(); j++) {
        char cur = 'a';
        for (int i = 0; i < (int) m.size(); i++) {
            if (m[i][j] < cur) { n++; break; }
            cur = m[i][j];
        }
    }
    return n;
}
