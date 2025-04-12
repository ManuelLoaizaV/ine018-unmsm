// Leer un número e imprimirle al usuario el doble de este.
// Terminar cuando el usuario ingrese un cero.

#include <iostream>
using namespace std;

int main(void) {
    int n;
    while (true) {
        cout << "Ingrese un número entero o cero para terminar: ";
        cin >> n;
        if (n == 0) break;
        int doble = 2 * n;
        cout << "El doble del número ingresado es " << doble << endl;
    }
    cout << "Programa terminado" << endl;
    return 0;
}