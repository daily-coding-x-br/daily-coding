// O(n), just going though the string recursively
#include <bits/stdc++.h>
using namespace std;

int biggestPath(string s, int &idx, int depth) {
    if (idx == (int) s.length()) return 0;

    // Skipping \t
    int i = idx;
    while (s[i] == '\t')
        i++;
    if (i-idx < depth) return -1;
    idx = i;

    // Parsing file/dir
    string aux;
    bool isFile = false;
    for (; idx < (int) s.length(); idx++) {
        if (s[idx] == '\n') { idx++; break; }
        if (s[idx] == '.') isFile = true;
        aux.push_back(s[idx]);
    }

    // Doing it recusively
    if (isFile) return aux.length();
    else {
        int ma = 0;
        int b;
        do {
            b = biggestPath(s, idx, depth+1);
            ma = max(ma, (int) aux.length() + 1 + b);
        } while (b != -1 && idx < (int) s.length());
        return ma;
    }
}

int main() {
    string s1 = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext";
    string s2 = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext";

    int idx = 0;
    cout << biggestPath(s1, idx, 0) << endl;
    idx = 0;
    cout << biggestPath(s2, idx, 0) << endl;
    return 0;
}
