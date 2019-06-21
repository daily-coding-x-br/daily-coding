#include <bits/stdc++.h>
using namespace std;

class Node {
public:
    bool isExp;
    char exp;
    int val;
    Node *l, *r;

    Node() {
        l = nullptr;
        r = nullptr;
    }

    Node(char e) : Node() {
        isExp = true;
        exp = e;
    }

    Node (int v) : Node() {
        isExp = false;
        val = v;
    }

    ~Node() {
        delete l;
        delete r;
    }
};

int evaluate(Node *n) {
    if (n == nullptr) return 0;
    if (!n->isExp) return n->val;
    switch (n->exp) {
        case '+':
            return evaluate(n->l) + evaluate(n->r);
            break;
        case '-':
            return evaluate(n->l) - evaluate(n->r);
            break;
        case '*':
            return evaluate(n->l) * evaluate(n->r);
            break;
        case '/':
            return evaluate(n->l) / evaluate(n->r);
            break;
        default:
            return 0;
    }
}

int main() {
    Node *n = new Node('*');
    n->l = new Node('+');
    n->r = new Node('+');
    n->l->l = new Node(3);
    n->l->r = new Node(2);
    n->r->l = new Node(4);
    n->r->r = new Node(5);
    cout << evaluate(n) << endl;
    return 0;
}
