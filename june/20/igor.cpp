// DP, O(n)
#include <bits/stdc++.h>
using namespace std;

int maxSum(vector<int> &v) {
    int ma = 0;
    int cur = 0;

    for (int i = 0; i < (int) v.size(); i++) {
        cur += v[i];
        if (cur < 0) cur = 0;
        ma = max(ma, cur);
    }

    return ma;
}

int main() {
    vector<int> v({34, -50, 42, 14, -5, 86});
    cout << maxSum(v) << endl;
    return 0;
}
