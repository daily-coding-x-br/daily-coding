// Storing a value and swapping it with probability 1 / count
#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long int ll;

ll llrand() {
    ll r = 0;
    for (int i = 0; i < 5; i++)
        r = (r << 15) | (rand() & 0x7FFF);
    return r & 0xFFFFFFFFFFFFFFFFULL;
}

int main() {
    int x;
    ll count;
    int stored;
    srand(time(NULL));

    cin >> x;
    stored = x;
    count = 1;
    cin >> x;
    while (x != 0) {
        if ((llrand() % ++count) == 0)
            stored = x;
        cin >> x;
    }
    cout << stored << endl;

    return 0;
}
