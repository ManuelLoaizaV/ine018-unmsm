#include <iostream>
#include <iomanip>
using namespace std;

// Calculamos la suma de Leibniz
// \sum_{k=0}^{n} \frac{(-1)^k}{2k + 1}
// la cual converge a PI/4 conforme n crece.
long double AproximarPi(int n) {
    long double suma = 0.0L;
    for (int k = 0; k <= n; k++) {
        long double fraccion = 1.0L / (2 * k + 1);
        if (k % 2 == 1) {
            fraccion *= -1.0L;
        }
        suma += fraccion;
    }
    long double pi = 4.0L * suma;
    return pi;
}

int main(void) {
    for (int n = 0; n <= 1000000; n++) {
        cout << "n = " << n;
        long double pi = AproximarPi(n);
        cout << " pi = " << fixed << setprecision(30) << pi << endl;
    }
    return 0;
}