// Using merge sort to count number of inversions (classical problem)
#include <bits/stdc++.h>
using namespace std;

int cnt;

void merge(vector<int> &v, int a, int m, int b) {
    vector<int> s;
    int i1 = a, i2 = m+1;
    while (i1 != m+1 && i2 != b+1) {
        if (v[i1] <= v[i2]) s.push_back(v[i1++]);
        else { s.push_back(v[i2++]); cnt += m-i1+1; }
    }
    while (i1 != m+1) s.push_back(v[i1++]);
    while (i2 != b+1) s.push_back(v[i2++]);
    for (int i = a; i <= b; i++)
        v[i] = s[i-a];
}

void mergeSort(vector<int> &v, int a, int b) {
    if (a == b) return;
    int m = (a+b)/2;
    mergeSort(v, a, m);
    mergeSort(v, m+1, b);
    merge(v, a, m, b);
}

int main() {
    vector<int> v({2, 4, 1, 3, 5}); 
    mergeSort(v, 0, 4);
    for (auto k : v)
        cout << k << " ";
    cout << endl << cnt << endl;
    return 0;
}
