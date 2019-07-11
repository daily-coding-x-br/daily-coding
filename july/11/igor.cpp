// Pa de coisa 9, mas com alguns elementos fora
#include <bits/stdc++.h>
using namespace std;

bool sumIs10(int a) {
    int s = 0;
    while (a > 0) {
        s += a % 10;
        a /= 10;
    }
    return s == 10;
}

int nPerfect(int n) {
    int a = 19;
    for (int i = 2; i <= n; i++) {
        a += 9;
        while (!sumIs10(a))
            a += 9;
    }
    return a;
}

int main() {
    int a;
    cin >> a;
    cout << nPerfect(a) << endl;
    return 0;
}
