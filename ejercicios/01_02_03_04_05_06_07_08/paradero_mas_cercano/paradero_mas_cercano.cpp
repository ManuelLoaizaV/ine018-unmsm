#include <iostream>

using namespace std;

int ObtenerParaderoMasCercano(int calle) {
    int izquierda = (calle / 8) * 8;
    int derecha = izquierda + 8;
    if (calle - izquierda <= derecha - calle) {
        return izquierda;
    }
    return derecha;
}

int main(void) {
    cout << ObtenerParaderoMasCercano(19) << endl;  // 16
    cout << ObtenerParaderoMasCercano(24) << endl;  // 24
    cout << ObtenerParaderoMasCercano(28) << endl;  // 24
    cout << ObtenerParaderoMasCercano(29) << endl;  // 32
    return 0;
}