// Using a stack for values and a stack for maximums
#include <bits/stdc++.h>
using namespace std;

class StackMax {
private:
    stack<int> s, m;

public:
    void push(int v) {
        s.push(v);
        m.push(std::max(m.top(), v));
    }

    void pop() {
        s.pop();
        m.pop();
    }

    int max() {
        return m.top();
    }
};

