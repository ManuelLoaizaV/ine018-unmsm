#include <iostream>
using namespace std;

int main(void) {
    // Leemos la nota del estudiante.
    int nota;
    cout << "Ingrese su nota entera: ";
    cin >> nota;

    // Convertimos la nota numérica a letras
    // utilizando la siguiente conversión:
    // https://gpa.eng.uci.edu/node/438
    if (nota < 0 || nota > 20) {
        cout << "La nota es invalida" << endl;
    } else if (nota >= 17) {
        cout << "A+" << endl;
    } else if (nota >= 15) {
        cout << "A" << endl;
    } else if (nota >= 13) {
        cout << "B" << endl;
    } else if (nota == 12) {
        cout << "C" << endl;
    } else if (nota == 11) {
        cout << "D" << endl;
    } else {
        cout << "Desaprobado" << endl;
    }

    return 0;
}
