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
    }

    ~Scheduler() {
        t->join();
        delete t;
    }

    void start() {
        t = new thread(&Scheduler::loop, this);
    }

    void loop() {
        while(1000.0 * (clock() - t0) / CLOCKS_PER_SEC < n)
            usleep(10);
        f(t0);
    }

    thread *t;
    time_t t0, n;
    void (*f)(time_t);
};

void foo(time_t t0) {
    cout << "Im called at " << 1000.0 * (clock() - t0) / CLOCKS_PER_SEC << "ms" << endl;
}

int main() {
    Scheduler s(123, &foo);
    s.start();
    cout << "Doing other stuff" << endl;
    return 0;
}
