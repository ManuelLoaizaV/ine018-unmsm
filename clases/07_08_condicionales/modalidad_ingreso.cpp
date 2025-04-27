#include <iostream>
using namespace std;

int main(void) {
    cout << "o: ordinario" << endl;
    cout << "c: cepre" << endl;
    cout << "p: primeros puestos" << endl;
    cout << "v: victima de terrorismo" << endl;
    cout << "Ingrese su modalidad de ingreso: ";

    char modalidad;
    cin >> modalidad;

    switch (modalidad) {
        case 'o':
            cout << "Lapicero";
            break;
        case 'c':
            cout << "Cuaderno";
            break;
        case 'p':
            cout << "Polo";
            break;
        case 'v':
            cout << "Gorra";
            break;
        default:
            cout << "ERROR";
            break;
    }
    cout << endl;
    return 0;
}