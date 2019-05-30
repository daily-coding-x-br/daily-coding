#include <bits/stdc++.h>
using namespace std;

string complete(string s, int k, int cnt, int spaceCnt) {
    if (cnt < k && spaceCnt == 0)
        return s + string(k-cnt, ' ');
    if (cnt < k) {
        int qtd = (k-cnt+spaceCnt) / spaceCnt; 
        int init = (k-cnt+spaceCnt) % spaceCnt; 
        int iCnt = 0;
        string res;
        for (char c : s) {
            if (c != ' ') res.push_back(c);
            else {
                if (iCnt++ < init) res += string(qtd+1, ' ');
                else res += string(qtd, ' ');
            }
        }
        return res;
    }
    return s;
}

vector<string> justify(vector<string> &v, int k) {
    vector<string> res;
    auto it = v.begin();
    int cnt = v[0].length(), spaceCnt = 0;
    res.push_back(v[0]);
    it++;
    while (it != v.end()) {
        if (cnt + (int) it->length() + 1 <= k) {
            res.back() += " ";
            res.back() += *it;
            cnt += (int) it->length() + 1;
            spaceCnt++;
        } else {
            res.back() = complete(res.back(), k, cnt, spaceCnt);;
            cnt = it->length();
            spaceCnt = 0;
            res.push_back(*it);
        }
        it++;
    }
    res.back() = complete(res.back(), k, cnt, spaceCnt);
    return res;
}

int main() {
    vector<string> v;
    string s;
    int n, k;
    cin >> n >> k;
    while (n--) {
        cin >> s;
        v.push_back(s);
    }

    auto jus = justify(v, k);
    for (auto j : jus)
        cout << j << endl;
    return 0;
}
