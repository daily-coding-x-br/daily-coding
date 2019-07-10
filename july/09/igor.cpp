// Two vectors for diagonals which count number of bishops
#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> d1, d2;
    int n, m;
    int tot = 0;
    int x, y;
    cin >> n >> m;
    d1.assign(2 * m, 0);
    d2.assign(2 * m, 0);
    while (n--) {
        cin >> x >> y;
        tot += d1[x+y];
        tot += d2[m+x-y];
        d1[x+y]++;
        d2[m+x-y]++;
    }
    cout << tot << endl;

    return 0;
}
