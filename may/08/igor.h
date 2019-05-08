#include <bits/stdc++.h>
using namespace std;

class Node {
public:
    Node(int v, Node* prev = nullptr, Node* next = nullptr);

    static Node *ptrXOR(Node *a, Node* b);

    int v;
    Node* both;
};

class List {
public:
    List();

    void add(int x);

    Node *get(int index);

private:
    Node *head;
};

class ListItr {
public:
    ListItr(List *l);

    void operator ++();

    void addNext(int v);

    Node *get();

    bool isEnd();

private:
    Node *a, *b, *c;
};
