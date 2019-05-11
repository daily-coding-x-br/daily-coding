#include<bits/stdc++.h>

using namespace std;

struct Node {
  int val;
  Node *left, *right;
  Node(int val, Node *left = nullptr, Node *right = nullptr)
      : val(val), left(left), right(right){};
};

long long ans = 0;

bool count(Node *node) {
    if(!node) return true;
    bool l = count(node->left), r = count(node->right);
    if(node->left and node->val != node->left->val) l = false;
    if(node->right and node->val != node->right->val) r = false;
    ans += (l and r);
    return (l and r);
}

int main () {
    Node root = Node(0, new Node(1), new Node(0, new Node(1, new Node(1), new Node(1)), new Node(0)));
    count(&root);
    cout << ans << endl;
}