#include <iostream>
#include <cmath>
using namespace std;

// Resuelve la ecuación ax^2 + bx + c = 0.
void ResolverEcuacionCuadratica(
    int a, int b, int c,
    int& n, long double& x1, long double& x2
) {
    // Calculamos Δ = b^2 - 4ac.
    int discriminante = b * b - 4 * a * c;

    // Inicialicemos nuestra variable asumiendo que no existen raíces reales.
    n = 0;

    // Si Δ > 0, tenemos dos raíces reales y diferentes:
    // x1 = (-b - √Δ) / 2a,
    // x2 = (-b + √Δ) / 2a.
    if (discriminante > 0) {
        n = 2;
        x1 = (-b - sqrt(discriminante)) / (2 * a);
        x2 = (-b + sqrt(discriminante)) / (2 * a);
    } else if (discriminante == 0) {
        // Si Δ = 0, tenemos una raíz real:
        // x = -b / 2a
        n = 1;
        x1 = -b / (2.0L * a);
    } else {
        // Si Δ < 0, ambas raíces son complejas con parte imaginaria no nula.
        // Como nuestra variable la habíamos inicializado en cero,
        // no hay que realizar ninguna modificación.
        n = 0;
    }
}

void ImprimirRaicesReales(int a, int b, int c) {
    int n;
    long double x1;
    long double x2;
    ResolverEcuacionCuadratica(a, b, c, n, x1, x2);
    cout << a << "x^2 + " << b << "x + " << c << " = 0" << endl;
    if (n == 0) {
        cout << "No tiene raices reales." << endl;
    } else if (n == 1) {
        cout << "Tiene una raiz real." << endl;
        cout << "x = " << x1 << endl;
    } else {
        cout << "Tiene dos raices reales." << endl;
        cout << "x1 = " << x1 << endl;
        cout << "x2 = " << x2 << endl;
    }
}

int main(void) {
    ImprimirRaicesReales(4,5,1);
    ImprimirRaicesReales(4,4,1);
    ImprimirRaicesReales(4,3,1);
    return 0;
}