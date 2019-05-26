#include <bits/stdc++.h>
using namespace std;

class Node {
public:
    Node(int v, Node* p) {
        this->v = v;
        l = nullptr;
        r = nullptr;
        this->p = p;
        locked = false;
    }

    ~Node() {
        delete l;
        delete r;
    }

    bool is_locked() {
        return locked;
    }

    bool lock() {
        if (is_locked()) return true;
        if (check_pos_down(this) && check_pos_up())
            locked = true;
        return locked;
    }

    bool unlock() {
        if (!is_locked()) return true;
        if (check_pos_down(this) && check_pos_up())
            locked = false;
        return !locked;
    }

private:
    int v;
    bool locked;
    Node *l, *r, *p;

    bool check_pos_down(Node* n) {
        if (n->is_locked()) return false;
        bool pos = true;
        if (n->l != nullptr) pos &= check_pos_down(n->l);
        if (n->r != nullptr) pos &= check_pos_down(n->r);
        return pos;
    }

    bool check_pos_up() {
        Node *k = this; 
        while (k != nullptr) {
            if (k->is_locked()) return false;
            k = k->p;
        }
        return true;
    }
};

