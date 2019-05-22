// After the intersecting nodes, everything is the same in the lists
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m, x;
    list<int> l1, l2;
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        cin >> x;
        l1.push_back(x);
    }
    for (int i = 0; i < m; i++) {
        cin >> x;
        l2.push_back(x);
    }

    auto it1 = l1.begin();
    auto it2 = l2.begin();
    if (l1.size() > l2.size())
        advance(it1, l1.size() - l2.size()); 
    else advance(it2, l2.size() - l1.size());

    while (*it1 != *it2) {
        it1++;
        it2++;
    }

    cout << *it1 << endl;

    return 0;
}
