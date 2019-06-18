// O(n), storing the minimum value until that point
#include <bits/stdc++.h>
using namespace std;

int maxProfit(vector<int> &v) {
    int mi = v[0];
    int r = -0x3f3f3f3f;
    for (int i = 1; i < (int) v.size(); i++) {
        r = max(r, v[i] - mi); 
        mi = min(mi, v[i]);
    }
    return r;
}

int main() {
    vector<int> v({9, 11, 8, 5, 7, 10});
    vector<int> v2({11, 10, 9, 8});
    cout << maxProfit(v) << endl;
    cout << maxProfit(v2) << endl;
    return 0;
}
