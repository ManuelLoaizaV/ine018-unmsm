#include <iostream>
using namespace std;

int main(void) {
    const int TOTAL_FEASTABLES = 100;

    cout << "Anthonny, tienes hambre (si / no)? ";
    string hambriento;
    cin >> hambriento;

    cout << "Ingrese el precio de un Feastable: ";
    double precio;
    cin >> precio;

    int feastables_a_comprar = 0;

    if (hambriento == "si") {
        if (precio < 1) {
            cout << "Compra todo" << endl;
            feastables_a_comprar = TOTAL_FEASTABLES;
        } else if (precio <= 3) {
            cout << "Compra diez" << endl;
            feastables_a_comprar = 10;
        } else {
            cout << "Compra uno" << endl;
            feastables_a_comprar = 1;
        }
    } else {
        cout << "No compres nada" << endl;
    }

    if (feastables_a_comprar >= 10) {
        cout << "Cajera: Asi que tienes mucha hambre, verdad?" << endl;
    }

    return 0;
}