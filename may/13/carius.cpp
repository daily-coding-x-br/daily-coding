#include<bits/stdc++.h>

using namespace std;

int main() {
    string s = "de";
    vector<string> w = {"do", "deer", "deal", "e"};
    sort(w.begin(), w.end());
    auto lb = lower_bound(w.begin(), w.end(), s);
    while(lb != w.end() and !s.compare(0,s.size(),*lb,0,s.size())) {
        cout << *lb << " ";
        lb++;
    }
    cout << endl;
    return 0;
}