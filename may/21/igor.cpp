// O(n*k). Keeping track of the sum using the last column's minimum and second minimum values. For each new column, calculate the 
// minimum sum and second minimum sum.
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, k;
    int m[1000][1000];
    cin >> n >> k;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < k; j++)
            cin >> m[i][j];

    int prevSumMin = 0, prevSumBMin = 0;
    int prevMinIdx = -1;
    int curMin = 0x3f3f3f3f, curBMin = 0x3f3f3f3f;
    int curIdx = 0;
    for (int i = 0; i < n; i++) {
        curMin = 0x3f3f3f3f;
        curBMin = 0x3f3f3f3f;
        curIdx = 0;

        for (int j = 0; j < k; j++) {
            int sum = (prevMinIdx == j) ? m[i][j] + prevSumBMin : m[i][j] + prevSumMin;

            if (curMin > sum) {
                curBMin = curMin;
                curMin = sum;
                curIdx = j;
            } else if (curBMin > sum)
                curBMin = sum;
        }

        prevSumMin = curMin;
        prevSumBMin = curBMin;
        prevMinIdx = curIdx;
    }

    cout << curMin << endl;

    return 0;
}
