#include <bits/stdc++.h>
using namespace std;

int rand7() {
    return rand() % 7 + 1;
}

int rand5() {
    int r = rand7();
    while (r > 5)
        r = rand7();
    return r;
}

int main() {
    srand(time(NULL));
    int cnt[] = {0, 0, 0, 0, 0};
    for (int i = 0; i < 1000000; i++)
        cnt[rand5()-1]++;
    for (int i = 0; i < 5; i++)
        cout << cnt[i] << endl;
    return 0;
}
