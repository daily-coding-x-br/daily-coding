// Counting number of r, g and b then its easy. I didnt understand the 
// "can only swap" instruction, we could just reconstruct the string.
#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    int rCnt = 0, gCnt = 0, bCnt = 0;
    
    cin >> s;
    for (auto c : s) {
        if (c == 'R') rCnt++;
        else if (c == 'G') gCnt++;
        else bCnt++;
    }

    int a = 0, b = rCnt, c = rCnt+gCnt;
    while (a != rCnt || b != rCnt+gCnt || c != rCnt+gCnt+bCnt) {
        if (a < rCnt && s[a] == 'R') a++;
        else if (b < rCnt+gCnt && s[b] == 'G') b++;
        else if (c < rCnt+gCnt+bCnt && s[c] == 'B') c++;
        else {
            if (a < rCnt) {
                if (s[a] == 'G') { swap(s[a], s[b]); b++; }
                if (s[a] == 'B') { swap(s[a], s[c]); c++; }
            } else if (b < rCnt+gCnt) {
                swap(s[b], s[c]);
                b++;
                c++;
            }
        }
    }
    cout << s << endl;

    return 0;
}
