#include <bits/stdc++.h>

using namespace std;

int main() {
    int N = 4;
    vector<int> dp(N+1,0);
    vector<int> X = {1,2};
    dp[0] = 1;
    for(int i = 0; i < N; i++) {
        for(int x : X)
            if(i+x<=N)
                dp[i+x]+=dp[i];
    }
    cout << dp[N] << endl;
}