#include <bits/stdc++.h>
using namespace std;

int rand7() {
    int x = 0;
    for (int i = 0; i < 7; i++)
        x += rand5();
    return x % 7 + 1;
}

