#include <bits/stdc++.h>
using namespace std;

bool isBalanced(string s) {
    stack<char> st;

    for (auto c : s) {
        if (c == '(' || c == '[' || c == '{')
            st.push(c);
        else if (c == ')') {
            if (st.empty() || st.top() != '(')
                return false;
            st.pop();
        } else if (c == ']') {
            if (st.empty() || st.top() != '[')
                return false;
            st.pop();
        } else if (c == '}') {
            if (st.empty() || st.top() != '{')
                return false;
            st.pop();
        }
    }
    if (!st.empty()) return false;
    return true;
}

int main() {
    string s;
    cin >> s;

    if (isBalanced(s)) cout << "True" << endl;
    else cout << "False" << endl;

    return 0;
}
