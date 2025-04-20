#include <algorithm>
#include <cmath>
#include <iostream>

using namespace std;

int main(void) {
    cout << "Valor absoluto" << endl;
    cout << "|5| = " << abs(5) << endl;
    cout << "|0| = " << abs(0) << endl;
    cout << "|-2.6| = " << abs(-2.6) << endl;

    cout << endl;
    cout << "Raíz cuadrada" << endl;
    cout << "sqrt(25) = " << sqrt(25) << endl;
    cout << "sqrt(1) = " << sqrt(1) << endl;
    cout << "sqrt(2) = " << sqrt(2) << endl;

    cout << endl;
    cout << "Suelo" << endl;
    cout << "floor(3.14) = " << floor(3.14) << endl;
    cout << "floor(5) = " << floor(5) << endl;
    cout << "floor(-6.7) = " << floor(-6.7) << endl;

    cout << endl;
    cout << "Logaritmos y exponenciales" << endl;
    cout << "log10(1000000) = " << log10(1000000) << endl;
    cout << "ln(e^5) = " << log(148.4131591) << endl;
    cout << "2^12 = " << pow(2, 12) << endl;
    cout << "e^5.7493929859 = " << exp(5.7493929859) << endl;

    cout << endl;
    cout << "Seno de 45 grados sexagesimales" << endl;
    cout << 1 / sqrt(2.0) << endl;
    cout << sin(0.785398) << endl;
    cout << sin(3.1415926535897932 / 4) << endl;
    const double pi = acos(-1);
    cout << sin(pi / 4) << endl;
    cout << sin(asin(1) / 2) << endl;
    cout << sin(45 * pi / 180) << endl;

    cout << endl;
    cout << "Máximo y mínimo" << endl;
    cout << max(4, 10) << endl;
    cout << max(-3, -1) << endl;
    cout << max(6, 6) << endl;
    cout << min(-7, 12) << endl;
    return 0;
}
