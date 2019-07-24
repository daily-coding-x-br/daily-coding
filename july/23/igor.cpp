#include <bits/stdc++.h>
using namespace std;

string read7() {
    return "";
}

class IStream {
private:
    queue<char> q;
public:
    string readN(int n) {
        int cnt = 0;
        string r;

        while (cnt < n) {
            if (q.empty()) {
                string read = read7();
                if (read.empty()) break;
                for (int i = 0; i < (int) read.length(); i++)
                    q.push(read[i]);
            }
            r.push_back(q.front());
            q.pop();
            cnt++;
        }

        return r;
    }
};
