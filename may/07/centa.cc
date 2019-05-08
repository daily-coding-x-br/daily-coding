#include <iostream>
#include <functional>

typedef std::function<int (std::function<int (int, int)>)> pair;

pair cons(int a, int b) {
    return ( [=] (std::function<int (int, int)> f) {
        return f(a, b);
    } );
}

int car(pair p) {
    return p( [] (int a, int b) { return a; } );
}

int cdr(pair p) {
    return p( [] (int a, int b) { return b; } );
}

int main() {
    // driver code
    std::cout << car(cons(3, 4)) << std::endl;
    std::cout << cdr(cons(3, 4)) << std::endl;

    return 0;
}