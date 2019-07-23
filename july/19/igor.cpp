// Using priority queue of fixed size k with the k first nodes from each list
#include <bits/stdc++.h>
using namespace std;

class Node {
public:
    int v;
    Node *n;

    Node(int v) {
        this->v = v;
        n = nullptr;
    }

    ~Node() {
        delete n;
    }
};

Node *mergeLists(vector<Node*> &v) {
    int k = v.size();
    auto comp = [](Node *a, Node *b) { return a->v > b->v; };
    priority_queue<Node*, vector<Node*>, decltype(comp)> pq(comp);
    Node *head = nullptr, *builder;

    for (int i = 0; i < k; i++)
        pq.push(v[i]);

    while (!pq.empty()) {
        Node *aux = pq.top();
        pq.pop();
        if (head == nullptr) {
            head = aux;
            builder = aux;
        } else {
            builder->n = aux;
            builder = builder->n;
        }

        if (aux->n != nullptr)
            pq.push(aux->n);
    }

    return head;
}

int main() {
    Node* h1 = new Node(1);
    h1->n = new Node(3);
    h1->n->n = new Node(5);
    Node* h2 = new Node(2);
    h2->n = new Node(4);

    vector<Node*> v({h1, h2});
    Node *r = mergeLists(v);
    Node *aux = r;
    while (aux != nullptr) {
        cout << aux->v << " ";
        aux = aux->n;
    }
    cout << endl;
    delete r;
    return 0;
}
