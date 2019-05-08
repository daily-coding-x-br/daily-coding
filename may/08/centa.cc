#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h> // for uintptr_t

struct Node {
    int data;
    Node *both;
};

// Returns the XOR of two Node pointers
Node *XOR(const Node *a, const Node *b) {
    return (Node *) (((uintptr_t) a)^((uintptr_t) b));
}

class XORLinkedList {
    private:
        Node *head, *tail;
    
    public:
        XORLinkedList() {
            head = tail = NULL;
        }

        // Add an element to the end
        void add(int element) {
            if (head == NULL) {
                tail = head = new Node;
                tail->data = element;
                tail->both = NULL; 
            }
            else {
                Node *added = new Node;
                added->data = element;
                added->both = tail;

                tail->both = XOR(tail->both, added);
                tail = added;
            }
        }

        // Get the element at index 
        int get(int index) {
            if (index == 0) return head->data;

            Node *curr = head->both;
            Node *prev =  head;
            int i = 1;
            while (i < index && curr != tail) {
                curr = XOR(curr->both, prev);
                ++i;
            }
            
            // return -1 if the index is out of range
            if (index < -1 || i < index) return -1;
            
            return curr->data;
        }
};

int main() {
    XORLinkedList list;

    // driver code
    list.add(1);
    list.add(2);
    list.add(4);
    
    printf("%d\n", list.get(0));
    printf("%d\n", list.get(2));
    printf("%d\n", list.get(4));
}