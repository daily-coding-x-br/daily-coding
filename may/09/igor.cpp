#include <bits/stdc++.h>
using namespace std;

string v;

int countDecodes(int i) {
    if (i == (int) v.size()) return 1;
    if (v[i] == '0') return -1;

    int jump1 = -1, jump2 = -1;
    jump1 = countDecodes(i+1);
    if (i < (int) v.size()-1 && 
        (v[i] == '1' || (v[i] == '2' && ('0' <= v[i+1] || v[i+1] <= '6'))))
        jump2 = countDecodes(i+2);
 
    if (jump1 == -1 && jump2 == -1) return -1;
    if (jump1 == -1) return jump2;
    if (jump2 == -1) return jump1;
    return jump1 + jump2;
}

int main() {
    cin >> v;
    cout << countDecodes(0) << endl;

    return 0;
}
