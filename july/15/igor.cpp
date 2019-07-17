// O(sqrt(x)), checking numbers until sqrt(x) if they
// are divisors of x and smaller than n
#include <bits/stdc++.h>
using namespace std;

int countNTimes(int n, int x) {
    int cnt = 0;
    for (int i = 1; i <= sqrt(x); i++)
        if (x % i == 0 && i <= n && x/i <= n)
                cnt += 2;
    return cnt;
}

int main() {
    cout << countNTimes(6, 12) << endl;
    return 0;
}
