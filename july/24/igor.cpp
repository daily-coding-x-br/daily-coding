#include <bits/stdc++.h>
using namespace std;

class Node {
public:
    char c;
    Node *l, *r;

    Node(char _c) {
        c = _c;
        l = nullptr;
        r = nullptr;
    }

    void print() {
        cout << c << " ";
        if (l != nullptr) l->print();
        if (r != nullptr) r->print();
    }

    ~Node() {
        delete l;
        delete r;
    }
};

void invert(Node *head) {
    if (head == nullptr) return;

    Node *aux = head->l;
    head->l = head->r;
    head->r = aux;

    invert(head->l);
    invert(head->r);
}

int main() {
    Node *head = new Node('a');
    head->l = new Node('b');
    head->r = new Node('c');
    head->l->l = new Node('d');
    head->l->r = new Node('e');
    head->r->l = new Node('f');
    head->print();
    cout << endl;
    invert(head);
    head->print();
    cout << endl;
    delete head;
    return 0; 
}
