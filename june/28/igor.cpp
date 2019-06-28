#include <bits/stdc++.h>
using namespace std;

vector<string> breakUp(string s, int k) {
    vector<string> v;
    string aux1, aux2;
    for (int i = 0; i < (int) s.length(); i++) {
        if (s[i] == ' ') {
            if ((int) aux1.length() + (int) aux2.length() < k) {
                if (!aux1.empty())
                    aux1.push_back(' ');
                aux1.append(aux2);
            } else {
                if ((int) aux2.length() > k) return {};
                v.push_back(aux1);
                aux1 = aux2;
            }
            aux2.clear();
        } else aux2.push_back(s[i]);
    }
    if ((int) aux1.length() + (int) aux2.length() < k) {
        aux1.append(aux2);
        v.push_back(aux1);
    } else {
        v.push_back(aux1);
        v.push_back(aux2);
    }
    return v;
}

int main() {
    string s = "the quick brown fox jumps over the lazy dog";
    auto v = breakUp(s, 10);
    for (int i = 0; i < (int) v.size(); i++)
        cout << v[i] << endl;
    return 0;
}
