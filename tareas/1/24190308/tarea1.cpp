#include <iostream>
using namespace std;

int main() {
    double A, B, C;
    cout << "Ingrese la primera nota:";
    cin >> A;
    cout << "Ingrese la segunda nota: ";
    cin >> B;
    cout << "Ingrese la tercera nota:";
    cin >> C; 

    double promedio = (A + B + C)/3;

    cout << "El promedio las notas: " << A << " , " << B << " y" << C << " es: " << promedio << endl;

    return 0;
}
