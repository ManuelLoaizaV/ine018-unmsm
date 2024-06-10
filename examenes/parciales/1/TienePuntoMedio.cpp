#include <iostream>
#include <algorithm>
using namespace std;

bool TienePuntoMedio(int x1, int x2, int x3) {
    // Encontramos el mayor y menor entre los tres números.
    int mayor = max(x1, max(x2, x3));
    int menor = min(x1, min(x2, x3));

    // Calculamos el valor medio como la suma menos los extremos.
    int medio = x1 + x2 + x3 - mayor - menor;

    // Verificamos si el valor medio equidista del mayor y el menor.
    return medio - menor == mayor - medio;
}

int main(void) {
    cout << TienePuntoMedio(4, 6, 8) << endl;
    cout << TienePuntoMedio(2, 10, 6) << endl;
    cout << TienePuntoMedio(8, 8, 8) << endl;
    cout << TienePuntoMedio(25, 10, -5) << endl;
    cout << TienePuntoMedio(3, 1, 3) << endl;
    cout << TienePuntoMedio(1, 3, 1) << endl;
    cout << TienePuntoMedio(21, 9, 58) << endl;
    cout << TienePuntoMedio(2, 8, 16) << endl;
    return 0;
}