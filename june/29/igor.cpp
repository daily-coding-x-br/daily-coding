#include <bits/stdc++.h>
using namespace std;

int searchRotated(vector<int> &v, int k) {
    int a = 0, b = (int) v.size() - 1;
    while (a < b) {
        int m = (a+b)/2;
        if (v[m] > v[0]) a = m+1;
        else b = m;
    }
    if (v[a] > v[0]) a++;
 
    if (v[0] > k) return lower_bound(v.begin() + a, v.end(), k) - v.begin();
    return lower_bound(v.begin(), v.begin() + a, k) - v.begin();
}

int main() {
    vector<int> v = {13, 18, 25, 2, 8, 10};
    cout << searchRotated(v, 8) << endl;
    return 0;
}
