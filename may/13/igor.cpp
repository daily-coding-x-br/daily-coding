// Creating a tree of prefixes
#include <bits/stdc++.h>
using namespace std;

class Node {
public:
    map<char, shared_ptr<Node>> m;
    bool isFinal;

    Node() {
        isFinal = false;
    }

    shared_ptr<Node> addChild(char c) {
        shared_ptr<Node> child;
        auto f = m.find(c);
        if (f == m.end()) {
            child = make_shared<Node>(); 
            m.insert({c, child});
        } else child = f->second;
        return child;
    }

    shared_ptr<Node> getChild(char c) {
        return m[c];
    }
};

class PrefixTree {
public:
    shared_ptr<Node> root;

    PrefixTree() {
        root = make_shared<Node>();
    }

    void setDict(vector<string> v) {
        for (auto s : v) {
            shared_ptr<Node> p = root;
            for (int i = 0; i < (int) s.length(); i++)
                p = p->addChild(s[i]); 
            p->isFinal = true;
        }
    }

    void autocomplete_rec(shared_ptr<Node> p, string &s, vector<string> &v) {
        if (p->isFinal)
            v.push_back(s);

        for (auto it : p->m) {
            s.push_back(it.first);
            autocomplete_rec(it.second, s, v);
            s.pop_back();
        }
    }

    vector<string> autocomplete(string s) {
        vector<string> v;
        shared_ptr<Node> p = root;
        for (int i = 0; i < (int) s.length(); i++)
            p = p->getChild(s[i]);

        autocomplete_rec(p, s, v);
        return v;
    }
};

int main() {
    vector<string> v;
    v.push_back("dog");
    v.push_back("deer");
    v.push_back("deal");

    PrefixTree pt;
    pt.setDict(v);

    auto cmp = pt.autocomplete("de");
    for (auto s : cmp)
        cout << s << " ";
    cout << endl;
    return 0;
}
