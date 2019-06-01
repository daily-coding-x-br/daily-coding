#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, x;
    vector<int> v;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> x;
        v.push_back(x);
    }

    int r = 0; 
    int lM = 0, rM = 0; 
    int a = 0, b = n-1; 
    while (a <= b)  { 
        if (v[a] < v[b]) { 
            if (v[a] > lM) 
                lM = v[a]; 
            else r += lM - v[a]; 
            a++; 
        } else { 
            if(v[b] > rM) 
                rM = v[b]; 
            else r += rM - v[b]; 
            b--; 
        } 
    } 

    cout << r << endl; 
    return 0;
}
