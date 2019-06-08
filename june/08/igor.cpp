// Complete search problem, O(2^n)
#include <bits/stdc++.h>
using namespace std;

vector<int> s, v;
vector<vector<int>> res;

void powerSet(int i) {
    if (i == (int) s.size())
        res.push_back(v);
    else {
        powerSet(i+1);
        v.push_back(s[i]);
        powerSet(i+1);
        v.pop_back();
    }
}

int main() {
    int n, x;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> x;
        s.push_back(x);
    }
    powerSet(0);

    for (auto r : res) {
        cout << "{";
        if (!r.empty())
            cout << r[0];
        for (int i = 1; i < (int) r.size(); i++)
            cout << ", " << r[i];
        cout << "} ";
    }
    cout << endl;

    return 0;    
}
