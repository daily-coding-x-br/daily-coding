// Adding bits of all numbers, and taking the sums modulo 3
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, x;
    vector<int> sums((int) 32);
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> x;
        for (int j = 0; j < 32; j++)
            if (x & (1 << j)) sums[j] = (1+sums[j]) % 3;
    }
    int r = 0;
    for (int j = 0; j < 32; j++)
        r += sums[j] * (1 << j);
    cout << r << endl;

    return 0;
}
