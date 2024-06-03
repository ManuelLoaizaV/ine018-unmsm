#include <iostream>
#include <iomanip>
using namespace std;

// Computa (1 + 1/n)^n la cual es cercana
// al número de Euler conforme n crece.
long double AproximarE(int n) {
    long double base = 1.0L + 1.0L / n;
    long double e = 1.0L;
    for (int i = 0; i < n; i++) {
        e *= base;
    }
    return e;
}

int main(void) {
    for (int n = 1; n <= 1000000; n++) {
        long double e = AproximarE(n);
        cout << "n = " << n;
        cout << " e = " << fixed << setprecision(30) << e << endl;
    }
    return 0;
}