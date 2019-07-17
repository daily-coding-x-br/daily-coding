// dp, O(n * maxValue)
#include <bits/stdc++.h>
using namespace std;
#define M 0x3f3f3f3f

int longSubsRec(int i, int cur, vector<int> &v, vector<vector<int>> &m) {
    if (i >= (int) v.size()) return 0;
    if (m[i][cur] != 0)
        return m[i][cur];

    int ma = longSubsRec(i+1, cur, v, m);
    if (v[i] >= cur)
        ma = max(ma, 1 + longSubsRec(i+1, v[i], v, m));
    m[i][cur] = ma;
    return ma;
}

int longSubs(vector<int> &v) {
    int ma = 0;
    for (int i = 0; i < (int) v.size(); i++)
        ma = max(ma, v[i]);
    vector<vector<int>> m;
    m.assign(v.size(), {});
    for (int i = 0; i < (int) v.size(); i++)
        m[i].assign(ma+1, 0);

    return longSubsRec(0, 0, v, m);
}

int main() {
    vector<int> v = {0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15};
    cout << longSubs(v) << endl;
    return 0;
}
