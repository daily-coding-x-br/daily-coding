// DP solution
#include <bits/stdc++.h>
using namespace std;

vector<vector<bool>> m; 
int sum;

bool dp(vector<int> &v, int idx, int curS) {
    if (idx == (int) v.size()) {
        if (curS == sum/2) return true;
        return false;
    }
    if (m[idx][curS]) return false; 

    if (dp(v, idx+1, curS)) return true;
    curS += v[idx];
    if (curS <= sum/2 && idx+1 < (int) v.size()) {
        if (dp(v, idx+1, curS)) return true;
        m[idx+1][curS] = true;
    }
    curS -= v[idx];
    return false;
}

bool splitSum(vector<int> &v) {
    sum = 0;
    for (auto k : v)
        sum += k;
    m.assign(v.size(), {});
    for (int i = 0; i < (int) v.size(); i++)
        m[i].assign(sum/2+1, false);

    return dp(v, 0, 0);
}

int main() {
    vector<int> v = {15, 5, 20, 10, 35, 15, 10};
    vector<int> v2 = {15, 5, 20, 10, 35};
    cout << splitSum(v) << endl;
    cout << splitSum(v2) << endl;
    return 0;
}
