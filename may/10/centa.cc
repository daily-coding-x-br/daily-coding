// O(n) runtime and O(1) space complexity with post order traversal
#include <iostream>

struct Node {
    int data;
    Node *left, *right;

    Node(int data) : data(data) {
        left = right = NULL;
    }

    Node(int data, Node *left, Node *right) :
        data(data), left(left), right(right) { }
};

bool check(Node *root, int& count) {
    bool ans = true;

    if (root->left != NULL &&
        (!check(root->left, count) ||
        root->left->data != root->data))
        ans = false;

    if (root->right != NULL &&
        (!check(root->right, count) ||
        root->right->data != root->data))
        ans = false;

    if (ans) ++count;

    return ans;
}

int count_universal_subtrees(Node *root) {
    int count = 0;

    if (root != NULL) check(root, count);

    return count;
}

int main() {
    Node *root  = new Node(0, new Node(1), new Node(0, new Node(1 , new Node(1), new Node(1)), new Node(0)));

    std::cout << count_universal_subtrees(root) << std::endl;

    return 0;
}