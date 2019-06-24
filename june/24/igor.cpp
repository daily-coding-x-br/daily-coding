#include <bits/stdc++.h>
using namespace std;

class Queue {
private:
    stack<int> s1, s2;

public:
    void enqueue(int k) {
        s1.push(k);
    }

    int dequeue() {
        if (!s2.empty()) {
            int k = s2.top();
            s2.pop();
            return k;
        }

        while (!s1.empty()) {
            s2.push(s1.top());
            s1.pop();
        }

        if (!s2.empty()) {
            int k = s2.top();
            s2.pop();
            return k;
        }
        else return -1;
    }
};

int main() {
    Queue q;
    q.enqueue(1);
    q.enqueue(2);
    q.enqueue(3);
    cout << q.dequeue() << endl;
    cout << q.dequeue() << endl;
    return 0;
}
