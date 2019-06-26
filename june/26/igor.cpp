#include <bits/stdc++.h>
using namespace std;

class URLShortener {
private:
    vector<string> m;

    string toKey(long idx) {
        // makes "aaaaaa" = 0 and "999999" = 62^6-1 
        string s = "aaaaaa";
        for (int i = 5; i >= 0; i--) {
            int k = idx % 62;
            if (k < 26) s[i] = k + 'a';
            else if (k < 52) s[i] = k + 'A';
            else s[i] = k + '0';
            idx /= 62;
        }
        return s;
    }

    long toIdx(string key) {
        // makes "aaaaaa" = 0 and "999999" = 62^6-1 
        long idx = 0;
        long p = 1;
        for (int i = 5; i >= 0; i--) {
            if ('a' <= key[i] && key[i] <= 'z')
                idx += p * (key[i] - 'a');
            else if ('A' <= key[i] && key[i] <= 'Z')
                idx += p * (key[i] - 'A' + 26);
            else idx += p * (key[i] - '0' + 52);
            p *= 62;
        }
        return idx;
    }

public:
    string shorten(string url) {
        auto it = lower_bound(m.begin(), m.end(), url);
        string r;
        if (it != m.end()) r = toKey(it - m.begin());
        else {
            r = toKey(m.size());
            m.push_back(url);
        }
        return r;
    }
    
    string restore(string key) {
        long idx = toIdx(key);
        if (idx >= (long) m.size())
            return "";
        return m[idx]; 
    }
};

int main() {
    URLShortener u;
    string ka = u.shorten("a");
    cout << ka << endl;
    string kb = u.shorten("b");
    cout << kb << endl;
    cout << u.restore(ka) << endl;
    cout << u.restore(kb) << endl;
    cout << u.shorten("a") << endl;
    return 0;
}
