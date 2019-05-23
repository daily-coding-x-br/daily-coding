// O(nlogn), sorting begginning and ending times and using a counter
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, x;
    vector<int> a, b;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> x;
        a.push_back(x);
    }
    for (int i = 0; i < n; i++) {
        cin >> x;
        b.push_back(x);
    }
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    int cnt = 0, ma = 0;
    int ia = 0, ib = 0;

    while (ia < n) {
        if (a[ia] < b[ib]) {
            cnt++;
            ma = max(ma, cnt);
            ia++;
        } else {
            cnt--;
            ib++;
        }
    }
    cout << ma << endl;

    return 0;
}
