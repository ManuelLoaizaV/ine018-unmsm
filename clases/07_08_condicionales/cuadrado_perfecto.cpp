#include <iostream>
#include <cmath>
using namespace std;

int main(void) {
    int n;
    cout << "Ingrese un número entero: ";
    cin >> n;

    if (n < 0) {
        cout << "La función raíz cuadrada no está definida para negativos" << endl;
        return 0;
    }

    int m = floor(sqrt(n));

    if (m * m == n) {
        cout << n << " = " << m << "^2" << endl;
    } else {
        cout << n << " no es cuadrado perfecto" << endl;
    }
    return 0;
}