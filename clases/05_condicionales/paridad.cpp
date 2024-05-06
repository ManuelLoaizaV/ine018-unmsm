#include <iostream>
using namespace std;

int main(void) {
    // Leemos la entrada del usuario.
    int n;
    cout << "Ingrese un numero entero: ";
    cin >> n;

    // Utilizamos el operador modulo para determinar la paridad.
    if (n % 2 == 0) {
        cout << n << " es par" << endl;
    } else {
        cout << n << " es impar" << endl;
    }
    return 0;
}