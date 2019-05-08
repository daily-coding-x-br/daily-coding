//O(n) time using only one array

#include<bits/stdc++.h>

using namespace std;

vector<int> prod(const vector<int> v) {
    int n = v.size();
    vector<int> r(n,1);
    int aux = 1;
    for(int i = 1; i < n; i++) {
        aux *= v[i-1];
        r[i] = aux;
    }
    aux = 1;
    for(int i = n-2; i >= 0; i--) {
        aux *= v[i+1];
        r[i] *= aux;
    }
    return r;
}

int main() {
    vector<int> test = {1,2,3,4,5};
    auto r = prod(test);
    for(auto x : r)
        cout << x << " ";
    cout << endl;
}