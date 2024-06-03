#include <iostream>
using namespace std;

int main(void) {
    int n;
    cout << "Ingrese el numero de impares: ";
    cin >> n;
    int suma = n * n;
    cout << "La suma de 1 + ... + " << 2 * n - 1 << " es " << suma << endl;
    return 0;
}