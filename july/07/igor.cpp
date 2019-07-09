#include <bits/stdc++.h>
using namespace std;

bool toss_biased() {
    return random() > 0.6 * RAND_MAX;
}

bool toss_unbiased() {
    while (true) {
        bool t1 = toss_biased();
        bool t2 = toss_biased();
        if (t1 && !t2) return true;
        else if (!t1 && t2) return false;
    }
}

int main() {
    int r = 0;
    for (int i = 0; i < 1000000; i++)
        r += toss_unbiased();
    cout << r / 1000000.0 << endl;
    return 0;
}
