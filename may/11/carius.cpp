/*
O(n) time, O(1) additional space

DP with two variables.
When processing the i-th value:
    a: best solution using the first i-2 values
    b: best solution using the first i-1 values
Answer: b at the end
*/
#include<bits/stdc++.h>

using namespace std;

int non_adj_sum(const vector<int> v) {
    int a,b;
    a = b = 0;
    for(int x : v) {
        int bb = b;
        b = max(b,max(a,a+x));
        a = bb;
    }
    return b;
}

int main () {
    vector<int> x = {2,4,6,2,5};
    vector<int> y = {5,1,1,5};
    cout << non_adj_sum(x) << endl;
    cout << non_adj_sum(y) << endl;
}