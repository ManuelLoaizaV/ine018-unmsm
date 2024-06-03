#include <iostream>
using namespace std;

int main(void) {
    double masa;
    cout << "Ingrese la cantidad de kilogramos de masa: ";
    cin >> masa;

    cout << "E = m * c^2" << endl;
    cout << "m = " << masa << " kg" << endl;

    double c = 2.99792459E8;
    cout << "c = " << c << " m/s" << endl;

    double E = masa * c * c;

    cout << E << " J de energía" << endl;
    return 0;
}