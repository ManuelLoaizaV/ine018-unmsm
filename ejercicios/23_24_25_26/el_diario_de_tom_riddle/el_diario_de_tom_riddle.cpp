#include <iostream>
#include <set>
using namespace std;

int main(void) {
    cout << "Ingrese el número de consultas: ";
    int consultas;
    cin >> consultas;

    set<string> portadores;

    for (int i = 1; i <= consultas; i++) {
        cout << "(" << i << ") Ingrese el nombre de la persona: ";
        string nombre;
        cin >> nombre;

        if (portadores.contains(nombre)) {
            cout << nombre << " ya abrió la cámara de los secretos" << endl;
        } else {
            cout << "Primera vez que el diario está en manos de " << nombre << endl;
            portadores.insert(nombre);
        }
    }
    return 0;
}
