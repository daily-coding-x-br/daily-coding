#include <bits/stdc++.h>
using namespace std;

int crosswords(vector<vector<char>> &m, string s) {
    for (int i = 0; i < (int) m.size(); i++) {
        string aux = "";
        for (int j = 0; j < (int) m[0].size(); j++)
            aux.push_back(m[i][j]);
        if (aux.find(s) != string::npos)
            return true;
    }

    for (int j = 0; j < (int) m[0].size(); j++) {
        string aux = "";
        for (int i = 0; i < (int) m.size(); i++)
            aux.push_back(m[i][j]);
        if (aux.find(s) != string::npos)
            return true;
    }

    return false;
}

int main() {
    vector<vector<char>> m;
    m.push_back({'F', 'A', 'C', 'I'});
    m.push_back({'O', 'B', 'Q', 'P'});
    m.push_back({'A', 'N', 'O', 'B'});
    m.push_back({'M', 'A', 'S', 'S'});
    cout << crosswords(m, "FOAM") << endl;
    return 0;
}
