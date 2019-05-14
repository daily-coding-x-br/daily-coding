//O(|W|*n)

#include <bits/stdc++.h>

using namespace std;

struct Node {
    int v;
    bool e;
    vector<int> g;
    Node() : g(26,-1), v(0), e(false) {}
    int& operator[](char c) { return g[c-'a']; }
};

vector<Node> trie(1);

void build(const string s) {
    int p = 0;
    trie[p].v++;
    for(char c:s) {
        if(trie[p][c] == -1)
            trie[p][c] = trie.size(), trie.push_back(Node());
        p = trie[p][c];
        trie[p].v++;
    }
    trie[p].e=true;
}

void dfs(int p, string& s) {
    if(trie[p].e)
        cout << s << " ";
    for(char c = 'a'; c <= 'z'; c++)
        if(trie[p][c]!=-1) {
            s.push_back(c);
            dfs(trie[p][c],s);
        }
    s.pop_back();
}

void query(const string s) {
    int p = 0;
    for(char c:s) {
        if(trie[p][c] == -1)
            return;
        p = trie[p][c];
    }
    string t = s;
    dfs(p,t);
}

int main() {
    string s = "de";
    vector<string> w = {"do", "deer", "deal", "e"};
    for(const string t : w)
        build(t);
    query(s);
    cout << endl;
    
    return 0;
}