// O(n). Using a map of used characters to their last known position
#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    int k;
    map<char, int> lastPos;
    int maxSize = 1;
    int start = 0;
    int numDist = 1;

    cin >> s >> k;
    for (int i = 1; i < (int) s.length(); i++) {
        if (lastPos[s[i]] == 0 && !(start == 0 && s[i] == s[0])) {
            if (numDist == k) {
                char erasing = s[start];
                while (start != lastPos[s[start]]) {
                    start++;
                    erasing = s[start];
                }
                start++;
                lastPos[erasing] = 0;
            } else numDist++;
        } 
        lastPos[s[i]] = i;
        maxSize = max(maxSize, i-start+1);
    }
    cout << maxSize << endl;
    return 0;
}
