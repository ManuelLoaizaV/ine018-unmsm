#include <iostream>
using namespace std;

int main(void) {
    int temperatura;
    cout << "Ingrese el valor de la temperatura del agua en Celsius: ";

    if (temperatura >= 100) {
        cout << "Ya hirvió el agua" << endl;
    }

    if (temperatura >= 1000) {
        cout << "Ya no hay agua, F" << endl;
    }

    if (temperatura > 2000) {
        temperatura = 2000;
    }

    if (temperatura < -2000) {
        temperatura = -2000;
    }

    cout << "La temperatura verdadera es " << temperatura << endl;

    return 0;
}