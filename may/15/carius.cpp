#include <bits/stdc++.h>

using namespace std;

unordered_set<int> hs;

int main() {
    string s = "abcba";
    int k = 2;
    int l = 0;
    int ans = 0;
    int id = 0;
    for(int i = 0; i < s.size(); i++) {
        hs.insert(s[i]);
        while(hs.size()>k)
            hs.erase(s[l++]);
        if(i-l+1>ans)
            ans = i-l+1, id = l;
    }
    cout << ans << " " << s.substr(id, ans) << endl;
}