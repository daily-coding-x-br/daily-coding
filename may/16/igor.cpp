// Scattering points inside the square (-1, -1)-(1, 1) and checking how many of
// them are in the circle
#include <bits/stdc++.h>
using namespace std;


int main() {
    int n = 10000000;

    double x, y;
    int cnt = 0;
    srand(time(NULL));
    auto total = RAND_MAX / 2;
    for (int i = 0; i < n; i++) {
        x = ((double) rand() / total) - 1;
        y = ((double) rand() / total) - 1;
        if (x * x + y * y < 1) cnt++;
    }

    double pi = 4.0 * cnt / n;
    cout << pi << endl;
    return 0;
}
