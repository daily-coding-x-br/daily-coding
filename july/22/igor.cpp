#include <bits/stdc++.h>
using namespace std;

vector<string> result;

void possibleStrings(vector<vector<char>> &map, string &digits, string cur) {
    int i = cur.size();
    vector<char> &pos = map[digits[i] - '0'];
    for (char k : pos) {
        cur.push_back(k);
        if (cur.size() == digits.size())
            result.push_back(cur);
        else possibleStrings(map, digits, cur);
        cur.pop_back();
    }
}

int main() {
    vector<vector<char>> map({{}, {}, {'a', 'b', 'c'}, {'d', 'e', 'f'}});
    string digits = "23";
    possibleStrings(map, digits, "");
    for (auto s : result)
        cout << s << endl;
    return 0;
}
