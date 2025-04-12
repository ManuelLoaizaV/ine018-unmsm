#include <iostream>
#include <cmath>
using namespace std;

/*
 * Tenemos el triangulo ABC.
 * Sea a el lado AB,
 * b el lado AC,
 * x el angulo en sexagesimales en el vertice A.
 * Calcular el area del triangulo ABC.
 */

int main(void) {
    // Leemos los datos del triangulo.    
    double x, a, b;
    cout << "Ingrese el angulo en sexagesimales: ";
    cin >> x;

    cout << "Ingrese los lados que rodean al angulo: ";
    cin >> a >> b;

    // Calculamos el valor de π.
    // La idea es ser lo más precisos posibles.
    // Alternativamente, pudimos utilizar std::numbers::pi de la biblioteca <numbers>.
    // Ver https://en.cppreference.com/w/cpp/numeric/constants
    const double PI = acos(-1);

    // Pasamos x de sexagesimales a radianes pues la función seno recibe angulos en radianes.
    x = x * PI / 180;

    // Calculamos e imprimimos el area del triangulo utilizando el teorema del seno.
    double area = a * b * sin(x) / 2;
    cout << "El area del triangulo es " << area << endl;
    return 0;
}