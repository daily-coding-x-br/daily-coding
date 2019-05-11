#include<bits/stdc++.h>

using namespace std;

struct Node {
  int val;
  Node *left, *right;
  Node(int val, Node *left = nullptr, Node *right = nullptr)
      : val(val), left(left), right(right){};
};

long long ans = 0;

long long count(Node *node) {
    if(!node) return 0;
    bool ok = true;
    long long l, r;
    l = count(node->left)+1, r = count(node->right)+1;
    if(l>1 and node->val != node->left->val) l = 0;
    if(r>1 and node->val != node->right->val) r = 0;
    ans += r*l;
    return l*r ? l*r : -1;
}

int main () {
    Node root = Node(0, new Node(1), new Node(0, new Node(1, new Node(1), new Node(1)), new Node(0)));
    count(&root);
    cout << ans << endl;
}