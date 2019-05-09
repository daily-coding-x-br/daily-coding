//DP with 2 variables, O(n) time, O(1) memory

#include <bits/stdc++.h>

using namespace std;

int main() {
    long long a,b;
    a = b = 1;
    char s,t;
    cin >> s;
    while(cin >> t) {
        long long c = b;
        if(s<'2' or (s=='2' and t<='6'))
            c += a;
        a = b, b = c, s = t;
    }
    cout << b << endl;
}