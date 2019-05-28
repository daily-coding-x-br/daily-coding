#include <bits/stdc++.h>
using namespace std;

class Node {
public:
    int v;
    Node *next;

    Node(int v, Node* n = nullptr) {
        this->v = v;
        next = n;
    }

    ~Node() {
        delete next;
    }

    void del(int k) {
        k--;
        Node *n = this;
        int cnt = 0;
        while (n->next != nullptr && cnt < k-1) {
            cnt++;
            n = n->next;
        }

        if (n->next == nullptr) return;
        if (cnt == k-1) {
            Node *aux = n->next;
            n->next = aux->next;
            aux->next = nullptr;
            delete aux;
        }
    }
};

int main() {
    int k = 3;

    Node *n4 = new Node(5);
    Node *n3 = new Node(4, n4);
    Node *n2 = new Node(3, n3);
    Node *n1 = new Node(2, n2);
    Node *root = new Node(1, n1);
    root->del(k);
    for (Node *n = root; n != nullptr; n = n->next)
        cout << n->v << " ";
    cout << endl;
    
    delete root;
    return 0;
}
