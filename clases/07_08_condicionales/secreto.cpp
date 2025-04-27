#include <iostream>
using namespace std;

int main(void) {
    cout << "Ingrese dos de los tres números: ";
    int x, y;
    cin >> x >> y;
    if (x != 1 && y != 1) {
        cout << "Falta 1" << endl;
    } else if (x != 2 && y != 2) {
        cout << "Falta 2" << endl;
    } else {
        cout << "Falta 3" << endl;
    }
    return 0;
}
