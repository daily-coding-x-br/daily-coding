// O(n^2) solution
#include <bits/stdc++.h>
using namespace std;

string longestPalN2(string s) {
    if (s.length() <= 1) return s;
    string maxS;

    // One element in center
    for (int i = 0; i < (int) s.length(); i++) {
        int m = min(i, (int) s.length() - i - 1);
        int j = 0;
        for (j = 0; j <= m; j++)
            if (s[i-j] != s[i+j]) break;
        j--;
        if (2 * j + 1 >= (int) maxS.length())
            maxS = s.substr(i-j, 2*j + 1);
    }

    // Two elements in center
    for (int i = 0; i < (int) s.length(); i++) {
        int m = min(i, (int) s.length() - i - 2);
        int j = 0;
        for (j = 0; j <= m; j++)
            if (s[i-j] != s[i+1+j]) break;
        j--;
        if (2 * j + 2 >= (int) maxS.length())
            maxS = s.substr(i-j, 2*j + 2);
    }

    return maxS;
}

int main() {
    cout << longestPalN2("aabcdcb") << endl;
    cout << longestPalN2("bananas") << endl;
    cout << longestPalN2("banaanas") << endl;
    return 0;
}
