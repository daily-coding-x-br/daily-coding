#include <bits/stdc++.h>
using namespace std;

class Node {
public:
    char c;
    Node *l, *r;

    Node(int _c) {
        c = _c;
        l = nullptr;
        r = nullptr;
    }

    ~Node() {
        delete l;
        delete r;
    }
};

// returns node and height
pair<Node*, int> deepest(Node *h) {
    if (h == nullptr) return {nullptr, 0};
    if (h->l == nullptr && h->r == nullptr) return {h, 0};
    
    pair<Node*, int> dl = deepest(h->l);
    pair<Node*, int> dr = deepest(h->r);
    if (dr.second > dl.second) return { dr.first, dr.second+1};
    else return { dl.first, dl.second+1};
}

int main() {
    Node *a = new Node('a');
    a->l = new Node('b');
    a->r = new Node('c');
    a->l->l = new Node('d');
    auto d = deepest(a);
    cout << d.first->c << " " << d.second << endl;
    return 0;
}
