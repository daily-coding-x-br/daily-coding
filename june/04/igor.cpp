// O(nlogn) keeping two heaps
#include <bits/stdc++.h>
using namespace std;

int main() {
    priority_queue<double> a;
    priority_queue<double, vector<double>, greater<double>> b;
    double x;
    double med = 0;

    while (cin >> x) {
        if (a.size() < b.size()) {
            if (x > med) {
                a.push(b.top());
                b.pop();
                b.push(x);
            } else a.push(x);
            med = (a.top() + b.top()) / 2.0;
        } else if (a.size() > b.size()) {
            if (x <= med) {
                b.push(a.top());
                a.pop();
                a.push(x);
            } else b.push(x);
            med = (a.top() + b.top()) / 2.0;
        } else {
            if (a.empty() || x <= med) { a.push(x); med = a.top(); }
            else { b.push(x); med = b.top(); }
        }

        cout << med << endl;
    }
    return 0;
}
