#include <bits/stdc++.h>
using namespace std;

int isAlmostNonDecreasing(vector<int> &v) {
    int cntDecr = 0;
    for (int i = 1; i < (int) v.size(); i++)
        if (v[i] < v[i-1]) {
            if (cntDecr > 0) return false;
            if (i-2 >= 0 && i+1 < (int) v.size() && 
                v[i-1] > v[i+1] && v[i] < v[i-2])
                return false;
            cntDecr++;
        }
    return true;;
}
