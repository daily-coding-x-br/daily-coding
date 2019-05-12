#include<bits/stdc++.h>

using namespace std;

chrono::steady_clock::time_point start;

void schedule(void (*f)(), int n) {
    this_thread::sleep_for(chrono::milliseconds(n));
    f();
}

void f() {
    cout <<"Time elapsed in ms: " << chrono::duration_cast<chrono::milliseconds>(chrono::steady_clock::now()-start).count() << endl;
}

int main() {
    start = chrono::steady_clock::now();
    schedule(f,123);
}