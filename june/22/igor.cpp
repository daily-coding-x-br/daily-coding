#include <bits/stdc++.h>
using namespace std;

int rand(int k) {
    return rand() % k;
}

// O(n), swapping each element with a random one from him til the end
vector<int> shuffle(vector<int> v) {
    int k = (int) v.size();
    for (int i = 0; i < k; i++)
        swap(v[i], v[i + rand(k-i)]);
    return v;
}

int score(vector<int> &v) {
    int r = 0;
    int p = 1;
    for (auto k : v) {
        r += k * p;
        p *= 10;
    }
    return r;
}

int main() {
    vector<int> v({1, 2, 3, 4}); 
    map<int, int> m;
    for (int i = 0; i < 1000000; i++) {
        auto aux = shuffle(v);
        m[score(aux)]++; 
    }
    for (auto key : m)
        cout << key.first << " " << key.second << endl;
    return 0;
}
