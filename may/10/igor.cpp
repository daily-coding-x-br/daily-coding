#include <bits/stdc++.h>
using namespace std;

class Node {
public:
    int v;
    Node *l, *r;

    Node(int v) {
        this->v = v;
        l = nullptr;
        r = nullptr;
    }
};

// Returns <count, value> of univaluesness. value = -1 if not
pair<int, int> getUnivalue(Node *n) {
    if (n == nullptr) return {0, 0};
    auto uvL = getUnivalue(n->l);
    auto uvR = getUnivalue(n->r);
    int cnt = uvL.first + uvR.first,
        val = -1;
    
    if ((n->l == nullptr && n->r == nullptr) ||
        (n->l == nullptr && uvR.second != -1 && n->v == uvR.second) ||
        (n->r == nullptr && uvL.second != -1 && n->v == uvL.second) ||
        (uvL.second != -1 && uvR.second != -1 &&
         n->v == uvL.second && n->v == uvR.second)) {
        cnt++;
        val = n->v;
    }

    return {cnt, val};
}

int main() {
    Node r(0), l1(1), r1(0), l2(1), r2(0), l3(1), r3(1);
    r.l = &l1;
    r.r = &r1;
    r1.l = &l2;
    r1.r = &r2;
    l2.l = &l3;
    l2.r = &r3;
    auto uv = getUnivalue(&r);
    cout << uv.first << endl;
    return 0;
}
