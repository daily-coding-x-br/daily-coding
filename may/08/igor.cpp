// The inverse operation of xor is xor, then if we have prev and want next, we do 
// both xor prev
#include "igor.h"

Node::Node(int v, Node* prev, Node* next) {
    this->v = v;
    both = ptrXOR(prev, next);
}

Node *Node::ptrXOR(Node *a, Node* b) {
    return (Node *) ((uintptr_t) a ^ (uintptr_t) b);
}

List::List() {
    head = nullptr;
}

void List::add(int x) {
    if (head == nullptr) {
        head = new Node(x, nullptr, nullptr);
        return;
    }

    ListItr it = ListItr(this);
    while (!it.isEnd())
        ++it;
    it.addNext(x);
}

Node *List::get(int index) {
    if (head == nullptr)
        return nullptr;
    if (index == 0)
        return head;

    ListItr it = ListItr(this);
    int i;
    for (i = 0; i < index && !it.isEnd(); i++)
        ++it;

    if (i != index) return nullptr;
    else return it.get();
}

ListItr::ListItr(List *l) {
    a = nullptr;
    b = l->get(0);
    c = Node::ptrXOR(a, b->both);
}

void ListItr::operator++() {
    if (b != nullptr && c != nullptr) {
        a = b;
        b = c;
        c = Node::ptrXOR(a, b->both);
    }
}

void ListItr::addNext(int v) {
    if (c == nullptr) {
        c = new Node(v, b);    
        b->both = Node::ptrXOR(a, c);
    } else {
        Node *d = Node::ptrXOR(b, c->both);
        Node *n = new Node(v, b, d);
        b->both = Node::ptrXOR(a, n);
        if (d != nullptr)
            d->both = Node::ptrXOR(n, Node::ptrXOR(c, d->both));
    }
}

Node *ListItr::get() {
    return b;
}

bool ListItr::isEnd() {
    return c == nullptr;
}

int main() {
    List l;
    l.add(0);
    l.add(1);
    l.add(2);
    l.add(3);
    cout << l.get(3)->v << endl;
    return 0;
}
