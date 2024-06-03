#include <iostream>
using namespace std;

int main(void) {
    double metros;
    cout << "Ingrese la distancia en metros: ";
    cin >> metros;

    double pulgadas = metros / 0.0254;
    double pies = pulgadas / 12;

    cout << "Distancia en pulgadas: " << pulgadas << endl;
    cout << "Distancia en pies: " << pies << endl;
    return 0;
}