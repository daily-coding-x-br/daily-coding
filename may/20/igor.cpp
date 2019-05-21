// Same thing as centa.py
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, k, x;
    vector<int> v;
    deque<int> q;
    cin >> n >> k;
    v.reserve(n);
    for (int i = 0; i < n; i++) {
        cin >> x;
        v.push_back(x);
    }

    for (int i = 0; i < k; i++) {
        while (!q.empty() && v[q.front()] <= v[i])
            q.pop_front();
        q.push_front(i);
    }

    for (int i = k; i < n; i++) {
        cout << v[q.back()] << " ";

        if (i - q.back() >= k)
            q.pop_back();

        while (!q.empty() && v[q.front()] <= v[i])
            q.pop_front();
        q.push_front(i);
    }
    cout << v[q.back()] << endl;

    return 0;
}
