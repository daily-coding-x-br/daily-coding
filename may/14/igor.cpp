// Dynammic programming, O(k*n)
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, k, x;
    vector<int> unq;
    vector<int> steps;

    cin >> n >> k;
    unq.assign(n+1, 0);
    steps.reserve(k);
    for (int i = 0; i < k; i++) {
        cin >> x;
        steps.push_back(x);
    }

    unq[0] = 1; 
    for (int i = 0; i < n; i++)
        for (int s : steps)
            if (i + s <= n)
                unq[i+s] += unq[i];

    cout << unq[n] << endl;
    return 0;
}
