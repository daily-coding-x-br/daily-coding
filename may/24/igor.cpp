#include <bits/stdc++.h>
using namespace std;

class Node {
public:
    char c;
    bool isEnd;
    map<char, shared_ptr<Node>> m;

    Node(char c) {
        this->c = c;
        isEnd = false;
    }

    shared_ptr<Node> add(char c) {
        if (m.find(c) == m.end())
            m[c] = make_shared<Node>(c);
        return m[c];
    }
};

vector<int> ans;
string s;
shared_ptr<Node> root;

bool getAns(int i, shared_ptr<Node> k) {
    if (i >= (int) s.length()) return true; 
    
    if (k->isEnd) {
        ans.push_back(i);
        if (getAns(i, root))
            return true;
        ans.pop_back();
    }
    if (i < (int) s.length())
        for (auto l : k->m)
            if (s[i] == l.second->c && getAns(i+1, l.second))
                return true;
    return false;
}

int main() {
    int n;
    root = make_shared<Node>(0);
    shared_ptr<Node> k;

    cin >> n;
    while (n--) {
        cin >> s;
        k = root;
        for (int i = 0; i < (int) s.length(); i++)
            k = k->add(s[i]);
        k->isEnd = true;
    }

    cin >> s;
    k = root;
    getAns(0, k);
    int i1 = 0;
    for (auto i2 : ans) {
        for (; i1 < i2; i1++)
            cout << s[i1];
        cout << " ";
    }
    for (; i1 < (int) s.length(); i1++)
        cout << s[i1];
    cout << endl;

    return 0;
}
