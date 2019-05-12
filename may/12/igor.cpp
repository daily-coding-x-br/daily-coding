// Note: compile with -lpthread flag
#include <bits/stdc++.h>
#include <unistd.h>
using namespace std;

class Scheduler {
public:
    Scheduler(int n, void (*f)(time_t)) {
        this->n = n;
        this->f = f;
        this->t0 = clock();
        thread t(&Scheduler::loop, this);
        t.join();
    }

    void loop() {
        while(1000.0 * (clock() - t0) / CLOCKS_PER_SEC < n)
            usleep(10);
        f(t0);
    }

    time_t t0, n;
    void (*f)(time_t);
};

void foo(time_t t0) {
    cout << "Im called at " << 1000.0 * (clock() - t0) / CLOCKS_PER_SEC << "ms" << endl;
}

int main() {
    Scheduler s(10, &foo);
    return 0;
}
