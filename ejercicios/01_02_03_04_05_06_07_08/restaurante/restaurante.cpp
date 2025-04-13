#include <iostream>
using namespace std;

int main(void) {
    int costo_plato = 0;
    cout << "Ingrese el costo del plato: ";
    cin >> costo_plato;

    double propina = 0.1 * costo_plato;
    double impuesto = 0.08 * costo_plato;
    double total = costo_plato + propina + impuesto;

    cout << "Propina: " << propina << endl;
    cout << "Impuesto: " << impuesto << endl;
    cout << "Monto total: " << total << endl;
    return 0;
}