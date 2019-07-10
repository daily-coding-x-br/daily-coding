// Finding three max and two min values on the list, then it becomes O(1) because 5 elements
#include <bits/stdc++.h>
using namespace std;

int maxOrMin(list<int> &l, bool m) {
    int v = 0x3f3f3f3f;
    if (m) v = -v;

    for (auto k : l) {
        if (m)
            v = max(v, k);
        else v = min(v, k);
    }
    l.erase(find(l.begin(), l.end(), v));
    return v;
}

int maxThreeProd(list<int> &l) {
    if (l.size() < 3) return 0;

    vector<int> candidates;
    candidates.push_back(maxOrMin(l, 1));
    candidates.push_back(maxOrMin(l, 1));
    candidates.push_back(maxOrMin(l, 1));
    if (!l.empty()) candidates.push_back(maxOrMin(l, 0));
    if (!l.empty()) candidates.push_back(maxOrMin(l, 0));

    int ma = -0x3f3f3f3f;
    for (int i = 0; i < (int) candidates.size()-2; i++)
        for (int j = i+1; j < (int) candidates.size()-1; j++)
            for (int k = j+1; k < (int) candidates.size(); k++)
                ma = max(ma, candidates[i] * candidates[j] * candidates[k]); 
    return ma;
}

int main() {
    list<int> l = {-10, -10, 5, 2};
    cout << maxThreeProd(l) << endl;
    return 0;
}
