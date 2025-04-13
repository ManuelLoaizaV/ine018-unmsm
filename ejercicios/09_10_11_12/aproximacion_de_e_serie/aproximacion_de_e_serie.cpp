#include <iostream>
#include <iomanip>
using namespace std;

// Computa \sum_{k=0}^n 1/k! la cual es cercana
// al número de Euler conforme n crece.
long double AproximarE(int n) {
    long long factorial = 1LL;
    long double e = 0.0L;

    for (long long k = 0LL; k <= n; k++) {
        if (k > 0) {
            factorial *= k;
        }
        long double fraccion = 1.0L / factorial;
        e += fraccion;
    }

    return e;
}

int main(void) {
    for (int n = 1; n <= 18; n++) {
        long double e = AproximarE(n);
        cout << "n = " << n;
        cout << " e = " << fixed << setprecision(30) << e << endl;
    }
    return 0;
}