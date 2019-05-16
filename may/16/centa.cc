#include <iostream>
#include <random>

double monte_carlo_estimate_pi(int n) {
    std::mt19937_64 gen(time(0));
    std::uniform_real_distribution<double> unif(-1.0, 1.0);
    
    int inside_circle = 0;
    for (int i = 0; i < n; ++i) {
        const double x = unif(gen);
        const double y = unif(gen);

        if (x*x + y*y < 1) ++inside_circle;
    }

    return (double) 4*inside_circle/n;
}

int main() {
    int n;

    std::cin >> n; // if n > 20.000 it usually gets it right for 3 digits

    std::cout << monte_carlo_estimate_pi(n) << std::endl;

    return 0;
}