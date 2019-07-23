// Sorting intervals then merging
#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> ii;

vector<ii> merge(vector<ii> &v) {
    vector<ii> r;
    if (v.empty()) return r;

    sort(v.begin(), v.end(), 
         [](ii a, ii b) { return a.first < b.first; });
    
    r.push_back(v[0]);
    for (int i = 1; i < (int) v.size(); i++) {
        if (r.back().second >= v[i].first) 
            r.back().second = max(r.back().second, v[i].second); 
        else r.push_back(v[i]);
    }
    
    return r;
}

int main() {
    vector<ii> v({{1, 3}, {5, 8}, {4, 10}, {20, 25}});
    auto r = merge(v);
    for (auto k : r)
        cout << "(" << k.first << ", " << k.second << ") ";
    cout << endl;
    return 0;
}
