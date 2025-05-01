#include <iostream>
using namespace std;

int main(void) {
    int l, r;
    cout << "Ingrese dos enteros l <= r: ";
    cin >> l >> r;

    // Inicializar
    int i = l;
    if (i % 2 != 0) {
        i++;
    }
    int cnt = 0;

    // Condicion
    while (i <= r) {
        cout << i << ' ';
        cnt++;
        // Actualizar
        i += 2;
    }

    if (cnt == 0) {
        cout << "No hay";
    }

    cout << endl;

    return 0;
}