#include<bits/stdc++.h>

using namespace std;

class XLinkedList {
    struct Node {
        int value;
        Node* both;
        Node(int value, Node* prev, Node *next) : value(value) , both(ptrXor(prev,next)) {};
        static Node* ptrXor(Node *a, Node *b) {
            return (Node*)(intptr_t(a)^intptr_t(b));
        }
    };
    Node *first, *last;
  public:
    XLinkedList() : first(nullptr), last(nullptr) {};
    void add(int value) {
        Node *temp = new Node(value, last, nullptr);
        if(last)
            last->both = Node::ptrXor(last->both, temp);
        else
            first = temp;
        last = temp;
    }
    int get(int p) {
        Node *temp = first, *prev = nullptr;
        for(int i = 0; i < p; i++) {
            if(temp == nullptr) throw("Out of range");
            auto aux = temp;
            temp = Node::ptrXor(prev, temp->both);
            prev = aux; 
        }
        if(temp == nullptr) throw("Out of range");
        return temp->value;
    }
};

int main() {
    XLinkedList list;
    list.add(1);
    list.add(2);
    list.add(3);
    list.add(4);
    for(int i = 0; i < 4; i++)
        cout << list.get(i) << endl;
}