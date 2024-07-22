#include <iostream>
#include <string>
using namespace std;

int main() {
    string a;
    cout << "Buen día, ingrese su código de estudiante: ";
    cin >> a;

    while (a != "24190307") {
        cout << "Este código no está registrado." << endl;
        cout << "Por favor, inténtelo de nuevo: ";
        cin >> a;
    }

    cout << "Bienvenida, Ariadna (" << a << ")." << endl;

    return 0;
}
// Primero probé con un valor que no era mi código, ya luego con el valor verdadero ^^