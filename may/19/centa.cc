// Let n be the number of directories and files in the filesystem'
// This solution has O(n) time and space complexity
#include <iostream>
#include <fstream>
#include <deque>
#include <string> 
#include <vector>

using namespace std;

struct Node {
    string name;
    int longest_path;

    vector<Node*> children;
};

int count_tabs(istream& str) {
    char tab;
    int num_tabs = 0;

    while (str.peek() == '\t') {
        str.get(tab);
        ++num_tabs;
    }

    return num_tabs;
}

// This function assumes that there is only one root (top-level directory)
Node *decode_filesystem(istream& filesystem) {
    deque<pair<int, Node*>> stack; 

    while (!filesystem.eof()) {
        const int curr_level = count_tabs(filesystem);

        // allocate memory for this node
        Node *curr = new Node; 

        // get name of this directory/file
        getline(filesystem, curr->name);

        // the longest path is initialized to -1
        curr->longest_path = -1;

        // pop stack until the parent is found
        while (!stack.empty() && stack.front().first >= curr_level)
            stack.pop_front();

        // add as a child if a parent exists
        if (!stack.empty()) {
            Node *parent = stack.front().second;

            parent->children.emplace_back(curr);
        }

        // add this node to the stack
        stack.emplace_front(curr_level, curr);
    }
    
    return stack.back().second;
}

bool is_file(Node *node) {
    return (node->name.rfind('.') != string::npos);
}

int longest_absolute_path_to_file(Node *root) {
    if (root->longest_path != -1) {
        return root->longest_path;
    }
    if (is_file(root)) {
        return root->name.length();
    }
    else {
        const int root_len = root->name.length();
        root->longest_path = 0;

        auto it = root->children.begin();
        while (it != root->children.end()) {
            const int childs_longest = longest_absolute_path_to_file(*it);

            if (childs_longest != 0)
                root->longest_path = max(childs_longest+root_len+1, root->longest_path);

            ++it;
        }

        return root->longest_path;
    }
}

int main() {
    ifstream filesystem("./input");

    Node *root = decode_filesystem(filesystem);

    cout << longest_absolute_path_to_file(root);

    return 0;
}

