#include <iostream>


struct Node {
    int data;
    Node *next;

    Node(int data, Node *next=nullptr);
};

void remove_kth_last(Node *head, int k) {
    // Keep a pointer to the element before the one we would
    // delete if curr was the end
    Node *curr, *prev_del, *del;

    // Start by advancing curr by k (guaranteed at least k length)
    for (int i = 0; i < k; ++i)
        curr = curr->next;
    prev_del = head;

    // Advance both until the end of the list
    while (curr->next != nullptr) {
        curr = curr->next;
        prev_del = prev_del->next;
    }

    // Delete the desired element
    del = prev_del->next;
    prev_del->next = prev_del->next->next;

    // Debug print the deleted element
    std::cout << del->data << std::endl;

    delete del;
}

int main() {
    int n, k;
    Node *head, *curr;

    std::cin >> n >> k;

    head = new Node(0);
    curr = head;

    for (int i = 1; i < n; ++i) {
        curr->next = new Node(i);
        curr = curr->next;
    }

    remove_kth_last(head, k);
}