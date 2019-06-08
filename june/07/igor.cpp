#include <bits/stdc++.h>
using namespace std;

class Node {
public:
    int v;
    Node *l, *r;

    Node(int v) {
        this->v = v;
        l = nullptr;
        r = nullptr;
    }

    ~Node() {
        delete l;
        delete r;
    }
};

Node* secondLargest(Node *root) {
    if (root == nullptr) return nullptr;
    if (root->r == nullptr && root->l == nullptr) return nullptr;

    Node *pt = root, *aux = nullptr;
    while (pt->r != nullptr) { 
        aux = pt; 
        pt = pt->r; 
    } 

    if (pt->l != nullptr) {
        aux = pt->l;
        while (aux->r != nullptr)
            aux = aux->r;
    }
    return aux;
}

int main() {
    Node *r = new Node(8);
    Node *l1 = new Node(3);
    Node *r1 = new Node(10);
    Node *ll1 = new Node(1);
    Node *rl1 = new Node(6);
    Node *rr1 = new Node(14);
    Node *lrl1 = new Node(4);
    Node *rrl1 = new Node(7);
    Node *lrr1 = new Node(13);
    r->l = l1;
    r->r = r1;
    l1->l = ll1;
    l1->r = rl1;
    rl1->l = lrl1;
    rl1->r = rrl1;
    r1->r = rr1;
    rr1->l = lrr1;
    cout << secondLargest(r)->v << endl;
    delete r;
    return 0;
}
