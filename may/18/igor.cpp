// Just using a vector to store orders
#include <bits/stdc++.h>
using namespace std;

class Recorder {
public:
    vector<int> ids;

    void record(int order_id) {
        ids.push_back(order_id);
    }

    int get_last(int i) {
        if (i < (int) ids.size())
            return ids[(int) ids.size() - i];
        else return -1;
    }
};
