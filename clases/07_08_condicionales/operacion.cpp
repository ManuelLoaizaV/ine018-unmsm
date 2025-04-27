#include <iostream>
using namespace std;

int main(void) {
    char operacion = '%';
    switch(operacion) {
        case '+':
            cout << "Suma" << endl;
            break;
        case '-':
            cout << "Resta" << endl;
            break;
        case '*':
            cout << "Multiplicacion" << endl;
            break;
        case '/':
            cout << "Division" << endl;
            break;
        default:
            cout << "La operacion no es ninguna de [+, -, *, /]." << endl;
            break;
    }
    return 0;
}