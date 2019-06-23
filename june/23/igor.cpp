// Using a double linked list and a map from values to adresses on the list.
// The first element on the list is the most recently used, 
// and the last is the least recently used.
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
        delete r;
    }
};

class LRUCache {
private:
    Node* root;
    Node* end;
    unordered_map<int, Node*> m;
    int n;
    int size;

public:
    LRUCache(int n) {
        root = nullptr;
        end = nullptr;
        this->n = n;
        size = 0;
    }

    void set(int key, int v) {
        if (m[key] != nullptr) {
            Node *aux = m[key]; 
            if (aux == root)
                root->v = v;
            else if (aux == end) {
                aux->l->r = nullptr;
                end = aux->l;
                root->l = aux;
                aux->r = root;
                root = aux;
            } else {
                aux->r->l = aux->l;
                aux->l->r = aux->r;
                aux->r = root;
                aux->l = nullptr;
                root = aux;
            }
        } else {
            if (root == nullptr) {
                root = new Node(v);
                end = root;
                size++;
            } else if (size < n) {
                root->l = new Node(v);
                root->l->r = root;
                root = root->l;
                size++;
            } else {
                Node* aux = end;
                end = end->l;
                end->r = nullptr;
                m.erase(aux->v);
                delete aux;
                root->l = new Node(v);
                root->l->r = root;
                root = root->l;
            }
            m[key] = root;
        }
    }

    int get(int key) {
        if (m[key] == nullptr) return -1;
        else {
            Node *aux = m[key];
            if (aux == root);
            else if (aux == end) {
                end->l->r = nullptr;
                end = end->l;
                aux->l = nullptr;
                aux->r = root;
                root->l = aux;
            } else {
                aux->l->r = aux->r;
                aux->r->l = aux->l;
                aux->l = nullptr;
                aux->r = root;
                root->l = aux;
            }
            root = aux;
            return root->v;
        }
    }
};

int main() {
    LRUCache lru(3);    
    lru.set(1, 1);
    lru.set(2, 2);
    lru.set(3, 3);
    cout << lru.get(1) << endl;
    cout << lru.get(2) << endl;
    cout << lru.get(3) << endl;
    cout << lru.get(4) << endl;
    lru.set(3, 3);
    cout << lru.get(1) << endl;
    lru.set(4, 4);
    cout << lru.get(2) << endl;
    return 0;
}
