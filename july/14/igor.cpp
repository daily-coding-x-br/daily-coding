#include <bits/stdc++.h>
using namespace std;

class Node {
public:
    int v;
    Node *r;
    Node(int _v) { v = _v; r = nullptr; }
    void print() {
        cout << v << " ";
        if (r == nullptr) cout << endl;
        else r->print();
    }
};

void reverse(Node* &head) {
    if (head == nullptr) return;

    Node *aux1 = head->r;
    head->r = nullptr;

    while (aux1 != nullptr) {
        Node *aux2 = aux1->r; 
        aux1->r = head;
        head = aux1;
        aux1 = aux2;
    }
};

int main() {
    Node *head = new Node(1);
    Node *n1 = new Node(2);
    Node *n2 = new Node(3);
    head->r = n1;
    n1->r = n2;

    head->print();
    reverse(head);
    head->print();
    return 0;
}
