#include <iostream>

using namespace std;

int main(void) {
    cout << "Ingrese su nombre: ";
    string nombre;
    cin >> nombre;

    cout << "Ingrese su edad: ";
    int edad;
    cin >> edad;

    cout << "Mi nombre es " << nombre << " y tengo " << edad << " años" << endl;
    return 0;
}