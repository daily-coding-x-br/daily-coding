// Using O(log y) solution, having a vector of all potencies of 2 of x
#include <bits/stdc++.h>
using namespace std;

double pow(int x, int y) {
    double r = 1;
    double pow = x;

    if (y < 0) {
        pow = 1.0 / x;
        y = -y;
    }

    while (y > 0) {
        if (y % 2) r *= pow;
        pow *= pow;
        y /= 2;
    }
    return r;
}

int main() {
    int x, y;
    cin >> x >> y;
    cout << pow(x, y) << endl;
    return 0;
}
