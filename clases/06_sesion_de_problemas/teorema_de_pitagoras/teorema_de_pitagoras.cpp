#include <iostream>
#include <cmath>
using namespace std;

int main(void) {
    double a, b;
    cout << "Ingrese los valores de los catetos: ";
    cin >> a >> b;
    double c = sqrt(a * a + b * b);
    cout << "Por el teorema de Pitagoras, la hipotenusa mide " << c << endl;
    return 0;
}