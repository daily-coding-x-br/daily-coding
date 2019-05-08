#include<bits/stdc++.h>

using namespace std;

auto cons(int a, int b) {
    return [=](auto f) {return f(a,b);};
}

template<typename T>
int car(T t) {
    return t([](int a, int b){return a;});
}

template<typename T>
int cdr(T t) {
    return t([](int a, int b){return b;});
}

int main() {
    auto t = cons(3,4);
    cout << car(t) << endl;
    cout << cdr(t) << endl;
}
